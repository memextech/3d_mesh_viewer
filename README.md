# 3D Mesh Visualizer

An interactive web application for visualizing 3D mesh files (STL and 3MF) built with Streamlit and Python.

## Features

- Support for STL and 3MF file formats
- Interactive 3D visualization with rotation, pan, and zoom capabilities
- Mesh analysis information:
  - Vertex and face count
  - Volume calculation
  - Surface area measurement
  - Watertight mesh verification
  - Color/material detection
- Scene support for complex 3D files
- Real-time visualization updates

## Technology Stack

- **Streamlit**: Web application framework
- **Trimesh**: 3D mesh processing library
- **Plotly**: Interactive 3D visualization
- **NumPy**: Numerical computations
- **NetworkX**: Graph operations for mesh analysis
- **LXML**: XML processing for 3MF files

## Installation

1. Ensure you have Python 3.11+ installed
2. Clone this repository
3. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

## Usage

1. Start the application:
   ```bash
   poetry run streamlit run app.py
   ```
2. Open your web browser and navigate to `http://localhost:8501`
3. Upload an STL or 3MF file using the file uploader
4. Interact with the 3D model using mouse controls:
   - Left click + drag: Rotate
   - Right click + drag: Pan
   - Scroll: Zoom

## Development

The project uses Poetry for dependency management. To add new dependencies:
```bash
poetry add package-name
```

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request