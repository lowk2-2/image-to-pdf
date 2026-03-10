# Image to PDF Converter

## Overview
This project provides a simple tool for converting images to PDF format.

## Features
- Supports multiple image formats (JPEG, PNG, BMP, etc.)
- Batch image processing
- Customizable output PDF settings

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/lowk2-2/image-to-pdf.git
   ```
2. Navigate to the project directory:
   ```bash
   cd image-to-pdf
   ```
3. Install the required dependencies:
   ```bash
   npm install
   ```

## Usage
To convert images to PDF, use the following command:
```bash
node converter.js input-image-path output-pdf-path
```
- `input-image-path`: Path to the image file or directory containing images.
- `output-pdf-path`: Path where the output PDF will be saved.

## Examples
### Convert a Single Image
```bash
node converter.js image.jpg output.pdf
```
### Convert Multiple Images
```bash
node converter.js images/ output.pdf
```

## Contributing
If you want to contribute to this project, please follow these steps:
- Fork the repository.
- Create a new branch: `git checkout -b feature/YourFeature`
- Commit your changes: `git commit -m 'Add new feature'`
- Push to the branch: `git push origin feature/YourFeature`
- Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, open an issue or contact the project maintainer.