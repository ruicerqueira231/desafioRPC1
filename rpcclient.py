import xmlrpc.client
import os
import base64

def connection_to_server():
    return xmlrpc.client.ServerProxy("http://localhost:6000/RPC2")

def rotate_image(encoded_image, proxy):
    try:
        rotated_image = proxy.rotate_image(encoded_image, 127)
        return rotated_image
    except Exception as e:
        print(f"Error: {e}")
        return None

def resize_image(encoded_image, proxy):
    try:
        resized_image = proxy.resize_image(encoded_image, 100, 100)
        return resized_image
    except Exception as e:
        print(f"Error: {e}")
        return None

def convert_to_grayscale(encoded_image, proxy):
    try:
        grayscale_image = proxy.convert_to_grayscale(encoded_image)
        return grayscale_image
    except Exception as e:
        print(f"Error: {e}")
        return None

def apply_blur(encoded_image, proxy):
    try:
        blurred_image = proxy.apply_blur(encoded_image)
        return blurred_image
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    proxy = connection_to_server()
    while True:
        print("\nMenu:")
        print("1. Rotate Image")
        print("2. Resize Image")
        print("3. Convert to Grayscale")
        print("4. Blur image")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            encoded_image = get_encoded_image()
            if encoded_image is not None:
                rotated_image = rotate_image(encoded_image, proxy)
                if rotated_image is not None:
                    save_image(rotated_image, "rotated_image.jpg")
                    print("Image rotated and saved as 'rotated_image.jpg'.")

        elif choice == "2":
            encoded_image = get_encoded_image()
            if encoded_image is not None:
                resized_image = resize_image(encoded_image, proxy)
                if resized_image is not None:
                    save_image(resized_image, "resized_image.jpg")
                    print("Image resized and saved as 'resized_image.jpg'.")

        elif choice == "3":
            encoded_image = get_encoded_image()
            if encoded_image is not None:
                grayscale_image = convert_to_grayscale(encoded_image, proxy)
                if grayscale_image is not None:
                    save_image(grayscale_image, "grayscale_image.jpg")
                    print("Image converted to grayscale and saved as 'grayscale_image.jpg'.")

        elif choice == "4":
            encoded_image = get_encoded_image()
            if encoded_image is not None:
                blurred_image = apply_blur(encoded_image, proxy)
                if blurred_image is not None:
                    save_image(blurred_image, "blurred_image.jpg")
                    print("Image blurred and saved as 'blurred_image.jpg'.")

        elif choice == "0":
            print("Thank for using the app! See you :)")
            break

        else:
            print("Invalid choice. Please try again.")

def get_encoded_image():
    image_filename = input("Enter image filename: ")

    if not os.path.isfile(image_filename):
        print(f"Error: File '{image_filename}' not found.")
        return None

    with open(image_filename, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    return encoded_image

def save_image(encoded_image, filename):
    with open(filename, "wb") as f:
        f.write(base64.b64decode(encoded_image.encode()))

if __name__ == "__main__":
    main()

