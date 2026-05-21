import cv2
import easyocr

reader = easyocr.Reader(['en'])

def preprocess_image(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    processed = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    return processed


def extract_text(image_path):

    processed = preprocess_image(image_path)

    result = reader.readtext(
        processed,
        detail=0
    )

    return "\n".join(result)