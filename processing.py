import torch
import clip
from transformers import BlipProcessor, BlipForConditionalGeneration
import re, os

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Loading CLIP model to ", device, "...")
model, preprocess = clip.load("ViT-B/32", device=device)




def CLIPClassify(imageobj, labels):


    try:
        image = imageobj
        text = clip.tokenize(labels).to(device)
        
        with torch.no_grad():          
            logits_per_image, logits_per_text = model(image, text)
            probs = logits_per_image.softmax(dim=-1).cpu().numpy() 
            
            best_match_idx = probs[0].argmax()
            print(labels[best_match_idx])
            return best_match_idx
    
    except Exception as e:
        print(f"❌ Error processing inputs for CLIP: {e}")
        return None



def BLIPFilename(imageobj, path):
    print("Loading BLIP model...")
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    BLIPmodel = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)
    try:
        raw_image = imageobj.convert('RGB')
        
        inputs = processor(raw_image, return_tensors="pt").to(device)
        out = BLIPmodel.generate(**inputs, max_new_tokens=20, repetition_penalty=1.2, no_repeat_ngram_size=2) # Generate a short caption
        caption = processor.decode(out[0], skip_special_tokens=True)
        
        file_name = caption.lower()
        file_name = re.sub(r'[^a-z0-9 ]', '', file_name)
        file_name = file_name.replace(' ', '_')
        file_name = file_name[:50]
        
        extension = os.path.splitext(path)[1]
        return f"{file_name}{extension}"
    
    except Exception as e:
        print(f"❌ Error converting image for BLIP: {e}")
        return "unknown_filename"


def add_to_folders(old_path, newfolder, newfilename):
    counter = 1
    os.makedirs(newfolder, exist_ok=True)
    new_path = os.path.join(newfolder, newfilename)
    while os.path.exists(new_path):
        name, ext = os.path.splitext(newfilename)
        new_path = os.path.join(newfolder, f"{name}_{counter}{ext}")
        counter += 1
    os.rename(old_path, new_path)
    
    print(f"✅ Moved to: {new_path}")