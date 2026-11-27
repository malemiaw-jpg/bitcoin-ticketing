
import qrcode
from pathlib import Path


# Folder where QR code images will be stored
QR_FOLDER = Path(__file__).parent / "static" / "images" / "qr"

# Create the folder if it doesn't exist
QR_FOLDER.mkdir(parents=True, exist_ok=True)


def generate_qr(data, filename):
    """
    Generate a QR code from supplied data.
    Save it inside static/images/qr.
    """

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    file_path = QR_FOLDER / filename

    image.save(file_path)

    return f"images/qr/{filename}"
