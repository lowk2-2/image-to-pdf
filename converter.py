import os
import sys
from PIL import Image
from pdf2image import convert_from_path
import PyPDF2
from pathlib import Path
from datetime import datetime

class ImagePDFConverter:
    def __init__(self):
        self.input_folder = "input"
        self.output_folder = "output"
        self.create_folders()
    
    def create_folders(self):
        """Create input and output folders if they don't exist"""
        os.makedirs(self.input_folder, exist_ok=True)
        os.makedirs(self.output_folder, exist_ok=True)
    
    def get_file_type(self, filename):
        """Detect file type based on extension"""
        ext = Path(filename).suffix.lower()
        if ext in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']:
            return 'image'
        elif ext == '.pdf':
            return 'pdf'
        return None
    
    def images_to_pdf(self):
        """Convert all images in input folder to a single PDF"""
        image_files = []
        
        for filename in os.listdir(self.input_folder):
            if self.get_file_type(filename) == 'image':
                image_files.append(os.path.join(self.input_folder, filename))
        
        if not image_files:
            print("No image files found in input folder.")
            return
        
        image_files.sort()
        images = []
        
        print(f"Converting {len(image_files)} image(s) to PDF...")
        for img_path in image_files:
            try:
                img = Image.open(img_path).convert('RGB')
                images.append(img)
                print(f"  ✓ Loaded: {os.path.basename(img_path)}")
            except Exception as e:
                print(f"  ✗ Error loading {os.path.basename(img_path)}: {e}")
        
        if images:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = os.path.join(self.output_folder, f"converted_images_{timestamp}.pdf")
            images[0].save(output_path, save_all=True, append_images=images[1:])
            print(f"✓ PDF created: {output_path}")
    
    def pdf_to_images(self):
        """Convert all PDFs in input folder to images"""
        pdf_files = []
        
        for filename in os.listdir(self.input_folder):
            if self.get_file_type(filename) == 'pdf':
                pdf_files.append(os.path.join(self.input_folder, filename))
        
        if not pdf_files:
            print("No PDF files found in input folder.")
            return
        
        for pdf_path in pdf_files:
            try:
                print(f"Converting: {os.path.basename(pdf_path)}")
                pages = convert_from_path(pdf_path)
                
                pdf_name = Path(pdf_path).stem
                output_subdir = os.path.join(self.output_folder, f"{pdf_name}_images")
                os.makedirs(output_subdir, exist_ok=True)
                
                for i, page in enumerate(pages, 1):
                    img_path = os.path.join(output_subdir, f"page_{i:03d}.png")
                    page.save(img_path, 'PNG')
                    print(f"  ✓ Saved: page_{i:03d}.png")
                
                print(f"✓ PDF converted to {len(pages)} image(s)\n")
            except Exception as e:
                print(f"✗ Error converting {os.path.basename(pdf_path)}: {e}\n")
    
    def convert(self):
        """Auto-detect and convert files"""
        has_images = any(self.get_file_type(f) == 'image' for f in os.listdir(self.input_folder))
        has_pdfs = any(self.get_file_type(f) == 'pdf' for f in os.listdir(self.input_folder))
        
        if not has_images and not has_pdfs:
            print("No supported files found in input folder.")
            print("Supported formats: PNG, JPG, JPEG, BMP, GIF, PDF")
            return
        
        print("=" * 50)
        print("Image-PDF Converter")
        print("=" * 50)
        
        if has_images:
            self.images_to_pdf()
        
        if has_pdfs:
            self.pdf_to_images()
        
        print("=" * 50)
        print("Conversion complete!")
        print("=" * 50)

if __name__ == "__main__":
    converter = ImagePDFConverter()
    converter.convert()