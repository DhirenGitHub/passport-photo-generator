# 📷 Passport Photo Generator

A Python application that generates passport-compliant photos by removing the background and replacing it with a solid color of your choice. Built with Tkinter for the GUI, rembg for background removal, and Pillow for image processing.

## ⭐ Introduction
This tool allows users to upload any photo, automatically remove the background using AI-powered segmentation, and replace it with a custom color to meet passport photo requirements. The simple GUI lets you preview adjustments and save the result directly.

## 🔧 Installation
### Prerequisites
- Python 3.x
- Tkinter
- Photos for processing

### Setup Instructions
  1. Clone the Repository
     
      ```bash
      git clone https://github.com/yourusername/passport-photo-generator.git
      cd passport-photo-generator
  2. Install Required Packages
      ```bash
      pip install rembg pillow

## 🤔 Code Overview
### Key Features
- Tkinter GUI with interactive preview
- Background removal using rembg's AI model (u2net_human_seg)
- Color picker integration for perfect background colors
- Auto-rotation handling with EXIF data correction

### Core Functionality
  1. Image Upload & Preview
  The GUI lets users select an image which is automatically resized and displayed:

      ```bash
      def UploadAction():
          global selectedFile, displayPic
          filename = filedialog.askopenfilename()
          displayPic = filename
          img = Image.open(displayPic).convert('RGBA')
          img = ImageOps.exif_transpose(img)  # Handle rotation
          img = img.resize((413, 531))  # Standard passport size
      
  2. Background Processing
  Using rembg's segmentation model to isolate the subject:
      ```bash
      def CreatePhoto():
          my_session = new_session("u2net_human_seg")
          output = remove(input, session=my_session)  # AI background removal
          background = Image.new('RGB', input.size, BgColor[0])
          background.paste(output, (0, 0), output)  # Combine with new background
      
  3. Color Selection
  Integrated color picker for perfect background matching:
      ```bash
      def choose_color():
          global BgColor
          color = colorchooser.askcolor(title="Choose background color")
          BgColor = color  # Stores RGB values for background
## 🖥️ Running the Application

### Launch the GUI with:
```bash    
python main.py
```

### Workflow:

1.  Click 'Open' to select a photo

2. Choose background color with 'BG Color'

3. Click 'Create' to generate passport photo

4. Result saves as passportphoto.jpg
