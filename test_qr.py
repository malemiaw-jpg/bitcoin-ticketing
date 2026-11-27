from qr_generator import generate_qr

qr_path = generate_qr(
    "This is a Bitcoin Ticketing test",
    "test_qr.png"
)

print("QR code generated:", qr_path)