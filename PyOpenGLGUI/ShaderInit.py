__author__ = 'zengjk'

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ctypes import c_void_p
from numpy import *

class vertex:
    # position array goes like:
    # array([[x0,y0,z0,1.0],[x1,y1,z1,1.0],[x2,y2,z2,1.0],...])
    # normal & texcoord array goes like:
    # array([[x0,y0,z0],[x1,y1,z1],[x2,y2,z2],...])
    def __init__(self,position,normal=None,texcoord=None):
        self.position = position
        self.normal = normal
        self.texcoord= texcoord

class OBJParser:
    def __init__(self,objfile):
        f = file(objfile)
        datas = f.readlines()
        #Coming Soon



class BaseShader:
    def __init__(self,vertex,vert_file,frag_file,indices=None):
        #By default we render use glDrawArrays; if indices is pointed out then we use glDrawElement instead.
        #vertex is an object, must contains positions, may contains colors or normals for each vertex
        self.vertex = vertex
        self.shader = self.createShader(vert_file,frag_file)
        self.indices = indices
        self.size_float = self.vert_comp = 4
        #use float32
        self.size_short = 2
    def createShader(self,vert_file,frag_file):
        shader = glCreateProgram()
        #load shader source files in string types as vert and frag
        vert_src,frag_src = self.loadfiles(vert_file,frag_file)
        vert = glCreateShader(GL_VERTEX_SHADER)
        frag = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(vert,vert_src)
        glShaderSource(frag,frag_src)
        glCompileShader(vert)
        glCompileShader(frag)
        glAttachShader(shader,vert)
        glAttachShader(shader,frag)
        glLinkProgram(shader)
        return shader
    def VAOInit(self):
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
    def VBOInit(self,vertex):
        datasize=(vertex.position).size+(vertex.normal).size+(vertex.texcoord).size
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER,vbo)
        glBufferData(GL_ARRAY_BUFFER,datasize*self.size_float,None,GL_STREAM_DRAW)
        glBufferSubData()
        glBindBuffer(GL_ARRAY_BUFFER,0)

