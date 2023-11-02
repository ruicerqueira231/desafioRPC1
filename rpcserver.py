from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from PIL import Image, ImageFilter
import io
import base64

# função que converte a imagem para cinza
def convert_to_grayscale(encoded_image):
    image_data = base64.b64decode(encoded_image.encode())
    image = Image.open(io.BytesIO(image_data))
    grayscale_image = image.convert("L")
    output_buffer = io.BytesIO()
    grayscale_image.save(output_buffer, format="JPEG")
    return base64.b64encode(output_buffer.getvalue()).decode()

#função que redimensiona a imagem -- recebe como parametros a imagem codificada e as dimensoes para redimensionar
def resize_image(encoded_image, width, height):
    image_data = base64.b64decode(encoded_image.encode())
    image = Image.open(io.BytesIO(image_data))
    image.thumbnail((width, height))
    output_buffer = io.BytesIO()
    image.save(output_buffer, format="JPEG")
    return base64.b64encode(output_buffer.getvalue()).decode()

#função que roda a imagem num certo angulo -- recebe como parametros a imagem codificada e o angulo
def rotate_image(encoded_image, angle):
    image_data = base64.b64decode(encoded_image.encode())
    image = Image.open(io.BytesIO(image_data))
    rotated_image = image.rotate(angle)
    output_buffer = io.BytesIO()
    rotated_image.save(output_buffer, format="JPEG")
    return base64.b64encode(output_buffer.getvalue()).decode()

#função que desfoca a imagem -- recebe como parametro a imagem codificada
def apply_blur(encoded_image):
    decoded_image = base64.b64decode(encoded_image)
    image = Image.open(io.BytesIO(decoded_image))
    blurred_image = image.filter(ImageFilter.GaussianBlur(5))
    buffered = io.BytesIO()
    blurred_image.save(buffered, format="JPEG")
    encoded_blurred_image = base64.b64encode(buffered.getvalue())
    return encoded_blurred_image.decode()

class CustomRequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

#registar servidor
server = SimpleXMLRPCServer(("0.0.0.0", 6000), requestHandler=CustomRequestHandler)
#permite ao cliente saber quais as funções que fazem parte do servidor
server.register_introspection_functions()

#registar funções
server.register_function(convert_to_grayscale, 'convert_to_grayscale')
server.register_function(resize_image, 'resize_image')
server.register_function(rotate_image, 'rotate_image')
server.register_function(apply_blur, 'apply_blur')

print("RPC Server is ready to accept requests...")
server.serve_forever()
