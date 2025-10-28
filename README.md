# 🖼️ AI Image Organizer: Smart Classification and Renaming

**AI Image Organizer** is a powerful, Python-based executable application designed to intelligently classify, organize, and optionally rename your image files using state-of-the-art multimodal AI models, **CLIP** and **BLIP**.

## ✨ Features

* **Intelligent Classification:** Uses advanced **CLIP** (Contrastive Language-Image Pre-training) and **BLIP** (Bootstrapping Language-Image Pre-training) models to understand image content and context.
* **Automatic Folder Creation:** Classifies images into relevant, automatically created folders (e.g., *Cats*, *Landscapes*, *Abstract*).
* **Path-Based Processing:** Simply enter the path to a folder containing your images, and the application handles the rest.
* **Flexible Renaming:** Optional feature to rename images based on their predicted class, ensuring file names are descriptive.
* **Standalone Executable:** Distribute and run the application easily without needing to manage complex Python dependencies.

---

## 🚀 Getting Started

### Prerequisites

Since this is a standalone executable, you should only need the following:

* **Operating System:** Windows, macOS, or Linux (depending on how the executable was bundled).
* **Input Directory:** A folder containing the images you wish to classify (supports common formats like `.jpg`, `.png`, `.webp`).

### Installation and Usage

1.  **Download:** Obtain the latest executable file (`ai_image_organizer.exe`, or similar) from the release page.
2.  **Run:** Double-click the executable file. A command-line interface (CLI) will open.
3.  **Input Path:** You will be prompted to enter the **absolute path** to the directory containing your images:
    ```
    Please enter the full path to the folder containing the images:
    > C:\Users\YourName\Desktop\Unsorted_Photos
    ```
4.  **Options:** Follow the prompts to select your preferences:
    * **Classification Strategy:** Choose which model (CLIP or BLIP) or a combination to use for classification.
    * **Renaming:** Choose whether to rename the files based on their predicted category.

---

## 🧠 How It Works

The core of this application relies on two powerful models:

### 1. Classification with CLIP

**CLIP** is used for its strong ability to match an image to a given set of text labels (classes).

* The model evaluates the similarity between the image and a predefined list of potential categories (e.g., *'a photo of a car'*, *'a drawing of a bird'*).
* The image is then placed into the folder corresponding to the label with the highest similarity score.

### 2. Context Generation with BLIP (Optional/Hybrid Use)

**BLIP** excels at generating descriptive captions for images.

* In advanced or hybrid modes, BLIP can generate a **contextual caption** for the image.
* This rich text description can then be used to further refine the classification, or it can be used to generate more descriptive filenames when the renaming option is selected.

---

## 🛠️ Configuration and Customization

The current executable is designed for simplicity, but if you have access to the underlying Python source code, you can customize:

* **Classification Labels:** Adjust the predefined list of categories (e.g., change *'Cats'* to *'Felines'* or add a new category like *'Food Photography'*).
* **Renaming Format:** Modify the template used for renaming files (e.g., change from `[Category]_[OriginalName]` to `[Date]_[Category]_[Index]`).
* **Model Parameters:** Fine-tune the confidence thresholds or temperature settings for the CLIP and BLIP models.

---

## 🛑 Troubleshooting

| Issue | Potential Solution |
| :--- | :--- |
| **App crashes immediately.** | Ensure your operating system meets the basic requirements. Try running the executable from the command line to see if an error message appears. |
| **Images not moving/classifying.** | Verify that the **path** you entered is correct and that the folder contains supported image files (`.jpg`, `.png`, etc.). Check the console output for any I/O errors. |
| **Classification is inaccurate.** | The AI models are highly capable but not perfect. Try adjusting the classification strategy (if available) or ensuring your image content aligns with the default categories the models were trained on. |

---

## 🤝 Contributing

(If this were an open-source project, you would include sections on how to contribute, file bug reports, and submit pull requests here.)

---

## 📜 License

This application is provided under the **[Insert License Type Here, e.g., MIT License]** license.

*Copyright (c) [Current Year] [Your Name or Organization Name]*
