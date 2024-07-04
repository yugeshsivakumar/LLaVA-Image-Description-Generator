# LLaVA-Image-Description-Generator
This project utilizes the LLaVA model, an end-to-end trained large multimodal model designed to understand and generate content based on both visual inputs (images) and textual instructions.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

The LLaVA Image Description Generator project aims to generate descriptive content for uploaded images using advanced AI techniques. It leverages the LLaVA model to interpret visual inputs and textual prompts, providing accurate and context-aware descriptions.

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

Before starting, ensure you have the following installed:
- Python 3.8.19
- install libraries

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yugeshsivakumar/LLaVA-Image-Description-Generator.git
cd LLaVA-Image-Description-Generator
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Install the ollama application from https://ollama.com/ according to the instructions provided on their website.
### Usage
To use the LLaVA Image Description Generator:

1. Start and install the LLaVA model using the command prompt:
```bash
ollama run llava
```
2. Run the Streamlit app:

```bash
streamlit run app.py
```
3. Access the app in your browser at http://localhost:8501.

4. Upload an image file (jpg, jpeg, png).

5. Enter a prompt or use the default prompt "Describe this image".

6. Click "Get Description" to see the generated description.

### Project Structure
The project structure includes:

- `app.py:` Streamlit application for interacting with the LLaVA model.
- `requirements.txt:` List of Python dependencies.
- `README.md:` Project documentation.
## Results

After generating descriptions, results can be visualized as follows:

<table>
  <tr>
    <td style="text-align:center">
      <img src="https://github.com/yugeshsivakumar/LLaVA-Image-Description-Generator/assets/156910899/3efe1ceb-9330-40bd-a4bd-f05f68798a12" alt="Result Image 1" style="width: 550px;">
      <br>
      <em>Result Image 1</em>
    </td>
    <td style="text-align:center">
      <img src="https://github.com/yugeshsivakumar/LLaVA-Image-Description-Generator/assets/156910899/3f51588f-d334-42a5-a0f6-cb3cb84076fd" alt="Result Image 2" style="width: 550px;">
      <br>
      <em>Result Image 2</em>
    </td>
  </tr>
</table>









### Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
