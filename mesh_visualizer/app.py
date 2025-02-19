import streamlit as st
import trimesh
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="3D Mesh Viewer",
    layout="wide"
)

st.title("3D Mesh Viewer")

def create_3d_preview(mesh):
    # Extract vertices and faces
    vertices = mesh.vertices
    faces = mesh.faces
    
    # Create the 3D mesh visualization
    mesh_color = '#e5ecf6'  # default color
    
    # Check if mesh has vertex colors
    if hasattr(mesh.visual, 'vertex_colors'):
        colors = mesh.visual.vertex_colors
        mesh_color = [f'rgb({c[0]},{c[1]},{c[2]})' for c in colors[:,:3]]
    # Check if mesh has face colors
    elif hasattr(mesh.visual, 'face_colors'):
        colors = mesh.visual.face_colors
        mesh_color = [f'rgb({c[0]},{c[1]},{c[2]})' for c in colors[:,:3]]
    
    fig = go.Figure(data=[
        go.Mesh3d(
            x=vertices[:, 0],
            y=vertices[:, 1],
            z=vertices[:, 2],
            i=faces[:, 0],
            j=faces[:, 1],
            k=faces[:, 2],
            vertexcolor=mesh_color if isinstance(mesh_color, list) else None,
            colorscale=None if isinstance(mesh_color, list) else [[0, mesh_color], [1, mesh_color]],
            intensity=vertices[:, 2] if not isinstance(mesh_color, list) else None,
            showscale=False
        )
    ])
    
    # Update the layout for better visualization
    fig.update_layout(
        scene=dict(
            aspectmode='data',
            camera=dict(
                up=dict(x=0, y=1, z=0),
                center=dict(x=0, y=0, z=0),
                eye=dict(x=1.5, y=1.5, z=1.5)
            ),
            xaxis=dict(showbackground=False),
            yaxis=dict(showbackground=False),
            zaxis=dict(showbackground=False),
            bgcolor='rgba(0,0,0,0)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False
    )
    
    return fig

# File uploader
uploaded_file = st.file_uploader("Choose a 3D model file", type=['stl', '3mf'])

if uploaded_file is not None:
    try:
        # Load the mesh or scene
        file_type = uploaded_file.name.split('.')[-1].lower()
        loaded_object = trimesh.load(uploaded_file, file_type=file_type)
        
        # Handle both single meshes and scenes
        if isinstance(loaded_object, trimesh.Scene):
            # Get the first mesh from the scene
            mesh_name = next(iter(loaded_object.geometry))
            mesh = loaded_object.geometry[mesh_name]
            st.sidebar.write(f"Loaded from scene: {mesh_name}")
        else:
            mesh = loaded_object
        
        # Create and display the 3D preview
        fig = create_3d_preview(mesh)
        st.plotly_chart(fig, use_container_width=True)
        
        # Display mesh information
        st.sidebar.header("Mesh Information")
        st.sidebar.write(f"File type: {file_type.upper()}")
        st.sidebar.write(f"Number of vertices: {len(mesh.vertices):,}")
        st.sidebar.write(f"Number of faces: {len(mesh.faces):,}")
        st.sidebar.write(f"Volume: {mesh.volume:.2f} cubic units")
        st.sidebar.write(f"Surface area: {mesh.area:.2f} square units")
        
        # Check if mesh has materials/colors
        has_colors = hasattr(mesh.visual, 'vertex_colors') or hasattr(mesh.visual, 'face_colors')
        st.sidebar.write(f"Has colors/materials: {'Yes' if has_colors else 'No'}")
        
        # Check if mesh is watertight
        st.sidebar.write(f"Is watertight: {'Yes' if mesh.is_watertight else 'No'}")
        
    except Exception as e:
        st.error(f"Error loading {file_type.upper()} file: {str(e)}")
        st.sidebar.error("Debug information:")
        st.sidebar.write(f"File type: {file_type}")
        st.sidebar.write(f"Error type: {type(e).__name__}")
        st.sidebar.write(f"Full error: {str(e)}")
else:
    st.info("Please upload an STL or 3MF file to view")
