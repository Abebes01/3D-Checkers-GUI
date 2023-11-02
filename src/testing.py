import ctypes
import fbx

from fbx import *

# Create an FBX manager
manager = FbxManager.Create()

# Create an IO settings object
io_settings = FbxIOSettings.Create(manager, IOSROOT)
manager.SetIOSettings(io_settings)

# Create a file importer
importer = FbxImporter.Create(manager, "")

# Specify the file to be imported
filename = "model.fbx"
if not importer.Initialize(filename, -1, manager.GetIOSettings()):
    print("Failed to initialize importer for " + filename)
    print("Error returned: " + importer.GetStatus().GetErrorString())
    exit(1)

# Create a scene object and import the file into it
scene = FbxScene.Create(manager, "myScene")
importer.Import(scene)

# Get the root node of the scene
root_node = scene.GetRootNode()

# Traverse the scene graph to extract the vertex data
vertices = []
normals = []
texcoords = []
for i in range(root_node.GetChildCount()):
    mesh_node = root_node.GetChild(i)
    if mesh_node.GetNodeAttribute().GetAttributeType() == FbxNodeAttribute.eMesh:
        mesh = mesh_node.GetNodeAttribute()
        for j in range(mesh.GetPolygonCount()):
            for k in range(3):
                vertex_index = mesh.GetPolygonVertex(j, k)
                vertices.append(mesh.GetControlPointAt(vertex_index))
                normals.append(mesh.GetPolygonVertexNormal(j, k))
                texcoords.append(mesh.GetTextureUV(vertex_index))

# Convert the vertex data to a numpy array
vertices = np.array(vertices, dtype=np.float32)
normals = np.array(normals, dtype=np.float32)
texcoords = np.array(texcoords, dtype=np.float32)

# Clean up the FBX objects
importer.Destroy()
scene.Destroy()
io_settings.Destroy()
manager.Destroy()















# import pygame

# from OpenGL.GL import *
# import pyassimp
# from pyrr import Matrix44
# from pyrr import fbx_loader

# # ... Create Pygame window ...

# scene = fbx_loader.load('model.fbx')
# mesh = scene.meshes[0]  # Assuming there's only one mesh in the scene

# vertices = mesh.vertices
# indices = mesh.faces

# vbo = glGenBuffers(1)
# glBindBuffer(GL_ARRAY_BUFFER, vbo)
# glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)

# ibo = glGenBuffers(1)
# glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibo)
# glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)

# # ... Create Pygame event loop ...

# while True:
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
#     # Set up model-view-projection matrix
#     mvp_matrix = Matrix44()
#     # ... Manipulate the matrix as needed ...
#     glMatrixMode(GL_MODELVIEW)
#     glLoadMatrixf(mvp_matrix.astype('f4'))
    
#     # Draw mesh
#     glEnableClientState(GL_VERTEX_ARRAY)
#     glBindBuffer(GL_ARRAY_BUFFER, vbo)
#     glVertexPointer(3, GL_FLOAT, 0, None)
    
#     glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibo)
#     glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)
    
#     glDisableClientState(GL_VERTEX_ARRAY)
    
#     pygame.display.flip()