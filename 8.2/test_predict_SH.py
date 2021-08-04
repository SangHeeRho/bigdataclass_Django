import pytest
from ml_sanghee import predict

@pytest.mark.parametrize("image_path, expected", [
    ("C:/sanghee/8.2/sample-3.png", 3),
    ("C:/sanghee/8.2/sample-4.png", 4),
    ("C:/sanghee/8.2/sample-6.png", 6),
    ("C:/sanghee/8.2/sample-7.png", 7),
    ("C:/sanghee/8.2/sample-8.png", 8)
])
def test_predict(image_path, expected):
    assert predict(image_path) == expected