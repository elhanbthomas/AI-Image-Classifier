# 🖼️ AI Image Organizer: Smart Classification and Renaming

**AI Image Organizer** is a powerful, Python-based application designed to intelligently classify, organize, and optionally rename your image files using state-of-the-art multimodal AI models, **CLIP** and **BLIP**.

## ✨ Features

* **Intelligent Classification:** Uses advanced **CLIP** (Contrastive Language-Image Pre-training) and **BLIP** (Bootstrapping Language-Image Pre-training) models to understand image content and context.
* **Automatic Folder Creation:** Classifies images into relevant, automatically created folders (e.g., *Cats*, *Landscapes*, *Abstract*).
* **Path-Based Processing:** Simply enter the path to a folder containing your images, and the application handles the rest.
* **Flexible Renaming:** Optional feature to rename images based on their predicted class, ensuring file names are descriptive.
* **Open Source Python Script:** Easily runnable and customizable via the `main.py` script.

---

## 🚀 Getting Started

Since this application runs directly from a Python script, you'll need to set up your environment first.

### Prerequisites

1.  **Python 3.8+:** Make sure you have a recent version of Python installed on your system.
2.  **Git:** Needed to clone the repository (optional, but recommended).

### Installation and Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/elhanbthomas/AI-Image-Classifier.git
    cd AI-Image-Classifier
    ```
    *(If you aren't using Git, just download the ZIP file and extract the contents.)*

2.  **Create a Virtual Environment (Recommended):**
    This isolates the project dependencies from your main Python installation.
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **Windows:**
        ```bash
        venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    All required packages, including `torch`, `transformers` (for CLIP/BLIP), and `Pillow`, are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  **Run the Application:**
    Ensure your virtual environment is active, then run the main script:
    ```bash
    python main.py
    ```

2.  **Input Path:**
    The application will prompt you to enter the **absolute path** to the directory containing your unsorted images:
    ```
    Please enter the full path to the folder containing the images:
    > C:\Users\YourName\Desktop\Unsorted_Photos
    ```

3.  **Options:**
    Follow the subsequent prompts to select your preferences, such as choosing between the **CLIP** or **BLIP** classification methods, and whether to enable the **renaming** feature.

---

## 🧠 How It Works

The core of this application relies on two powerful multimodal AI models:

### 1. Classification with CLIP
**CLIP** is used for its superior ability to match an image to a given set of text labels (classes). It calculates the similarity between the image features and the category text embeddings, placing the image into the folder corresponding to the best match.

### 2. Context Generation with BLIP
**BLIP** is used to generate a rich, descriptive caption for the image. This caption can be leveraged in a hybrid classification mode for better context or directly used to create highly descriptive filenames when the renaming option is activated.

---

## 🛠️ Customization

Since you have access to the source code, you can easily modify the behavior:

* **Classification Labels:** Edit the list of target classification categories within `main.py` to tailor it to your specific needs.
* **Renaming Format:** Adjust the string template in the code that dictates how files are renamed (e.g., using date, category, and index).
* **Model Parameters:** Advanced users can modify the confidence thresholds or fine-tune model loading parameters to optimize performance on specific hardware (like using a GPU if available).

---

## 🛑 Troubleshooting

| Issue | Potential Solution |
| :--- | :--- |
| **`ModuleNotFoundError`** | Make sure you activated your virtual environment and ran `pip install -r requirements.txt` successfully. |
| **Slow Performance** | Classification using CLIP/BLIP is computationally intensive. Ensure you have a recent CPU, and if possible, run the script on a machine with an NVIDIA **GPU** and the appropriate **CUDA** drivers installed for a significant speed boost. |
| **Inaccurate Classification** | Review the hard-coded classification labels in the script. Ensure they are clear and descriptive, helping the AI models categorize correctly. |

---

## 📜 License

This application is provided under the **MIT License** license.

*Copyright (c) 2025 Elhan B Thomas.*
