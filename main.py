print("Starting main program...")

import os
from PIL import Image

from processing import CLIPClassify, BLIPFilename, device, preprocess, add_to_folders

# LABELS = [
#     "code editor",
#     "terminal command line",
#     "web browser",
#     "web page",
#     "json api data",
#     "pdf document",
#     "social_media",
#     "email client",
#     "chat messaging",
#     "document editor",
#     "video conference",
#     "file manager",
#     "settings configuration",
#     "diagram chart graphs",
#     "design software",
#     "people",
#     "tables spreadsheets",
#     "texts paragraphs",
#     "dialogue boxes"
#     "other"
# ]

LABELS = [
    # CODE EDITOR
    "a screenshot of computer code with colored text",
    "a user interface with line numbers and a text editor",
    "a photo of a software development environment (IDE)",
    "screenshot of a code editor",
    
    # TERMINAL COMMAND LINE
    "a screenshot of a command line interface (CLI)",
    "a photo of a terminal window with text commands",
    "a user interface with a command prompt",
    "screenshot of a terminal command line",
    
    # WEB BROWSER
    "a screenshot of a web browser with a tab bar and address bar",
    "a user interface with tabs at the top and a URL bar",
    "a computer screen showing a website with browser controls",
    "screenshot of a web browser",
    
    # WEB PAGE
    "a screenshot of a webpage with text and images",
    "a photo of a website's content",
    "an image of an article on the internet",
    "screenshot of a web page",
    
    # PDF DOCUMENT
    "a screenshot of a social media app like Twitter or Instagram",
    "a user interface with a social media feed",
    "an image of a post from a social networking site",
    "screenshot of a pdf document opened in a viewer like edge or adobe",
    
    # SOCIAL MEDIA
    "a screenshot of a social media app like Twitter or Instagram",
    "a user interface with a social media feed",
    "an image of a post from a social networking site", 
    
    # EMAIL CLIENT
    "a screenshot of an email application like Gmail or Outlook",
    "a user interface showing an email inbox",
    "an image of an email client with a list of messages"
    
    # CHAT MESSAGING
    "a screenshot of a chat or messaging app",
    "a user interface showing a conversation with message bubbles",
    "an image of a direct messaging application",
    
    # DOCUMENT EDITOR
    "a screenshot of a document editor like Microsoft Word or Google Docs",
    "a user interface with a toolbar for editing text",
    "an image of a word processing application",
    "screeshot of presentation software with slides",
    
    # VIDEO CONFERENCE
    "a screenshot of a video conference call on Zoom or Google Meet",
    "a user interface with multiple video feeds of people",
    "an image of a virtual meeting in progress",
    
    # FILE MANAGER
    "a screenshot of a file manager or finder window",
    "a user interface showing a list of files and folders",
    "an image of a computer's file explorer",
    
    # SETTINGS CONFIGURATION
    "a screenshot of a settings or configuration panel",
    "a user interface with toggles, sliders, and checkboxes",
    "an image of a system preferences window",
    
    # DIAGRAM CHART GRAPHS
    "a screenshot of a diagram, chart, or graph",
    "a data visualization like a bar chart or pie chart",
    "an image of a flowchart or mind map",
    
    # DESIGN SOFTWARE
    "a screenshot of design software like Figma or Photoshop",
    "a user interface for graphic design with a canvas and tools",
    "an image of a digital design application",
    
    # PEOPLE
    "a photo of a person or a group of people",
    "a portrait of a person's face",
    "an image featuring people",
    
    # TABLES SPREADSHEETS
    "a screenshot of a spreadsheet with rows and columns",
    "a photo of a table with data",
    "an image of a spreadsheet application like Excel or Google Sheets",
    
    # TEXTS PARAGRAPHS
    "a screenshot of a block of text or a paragraph",
    "an image focusing on written text",
    "a photo of a page from a book or article",
    
    # DIALOGUE BOXES
    "a screenshot of a dialogue box, popup, or alert",
    "a user interface with a modal window asking for confirmation",
    "an image of a notification popup on a computer screen",
    
    # LANDSCAPES NATURE
    "a photo of a natural landscape with trees, mountains, or water",
    "an image of outdoor scenery like forests or beaches",
    "a picture showcasing nature and wildlife",
    
    # SHOPPING ECOMMERCE
    "a screenshot of an online shopping website or app",
    "a user interface showing products for sale",
    "an image of an e-commerce platform with a shopping cart",
]

def getFolderName(index):
    if index is None:
        return None
    if index in range(0,4):
        return "code_editor"
    elif index in range(4,8):
        return "terminal_command_line"
    elif index in range(8,12):
        return "web_browser"
    elif index in range(12,16):
        return "web_page"
    elif index in range(16,20):
        return "pdf_document"
    elif index in range(20,23):
        return "social_media"
    elif index in range(23,26):
        return "email_client"
    elif index in range(26,29):
        return "chat_messaging" 
    elif index in range(29,32):
        return "document_editor"
    elif index in range(32,35):
        return "video_conference"
    elif index in range(35,38):
        return "file_manager"
    elif index in range(38,41):
        return "settings_configuration"
    elif index in range(41,44):
        return "diagram_chart_graphs"
    elif index in range(44,47):
        return "design_software"
    elif index in range(47,50):
        return "people"
    elif index in range(50,53):
        return "tables_spreadsheets"
    elif index in range(53,56):
        return "texts_paragraphs"
    elif index in range(56,59):
        return "dialogue_boxes"
    elif index in range(59,62):
        return "landscapes_nature"
    elif index in range(62,65):
        return "shopping_ecommerce"

def organize_files(folder_path, rename):
    print("\nScanning for files...")
    supported_formats = ('.png', '.jpg', '.jpeg')
    print("Categorizing...\n")
    try:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(supported_formats):
                filepath = os.path.join(folder_path, filename)
                image = Image.open(filepath)
                
                processed_image = preprocess(image).unsqueeze(0).to(device)
            
                index = CLIPClassify(processed_image, LABELS)
                folder_name = getFolderName(index)
                # print(f"{filename} Classified as: {folder_name}")
                if rename:
                    new_filename = BLIPFilename(image, filepath)
                    # print(f"New filename for {filename}: {new_filename}")
                    
                    if folder_name and new_filename:
                        dest_folder = os.path.join(folder_path, folder_name)
                        add_to_folders(filepath, dest_folder, new_filename)
                else:
                    if folder_name:
                        dest_folder = os.path.join(folder_path, folder_name)
                        add_to_folders(filepath, dest_folder, filename)
                    
                
    except Exception as e:
        print(f"❌ Error accessing folder: {e}")
        return
    
def main():
    target_folder = input("\nEnter the target folder path: ")
    rename = input("Do you want to rename files based on content? (y/n): ").lower() == 'y'
    if not os.path.isdir(target_folder):
        print(f"❌ Error: The path '{target_folder}' is not a valid directory.")
        return

    organize_files(target_folder, rename)
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()