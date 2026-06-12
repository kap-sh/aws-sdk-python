"""Generated from Smithy shape ``com.amazonaws.rekognition#ImageQuality``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.float


class ImageQuality(TypedDict):
    brightness: NotRequired["aws_sdk_rekognition.types.float.Float"]
    """<p>Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.</p>"""
    sharpness: NotRequired["aws_sdk_rekognition.types.float.Float"]
    """<p>Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageQuality) -> dict:
    out: dict = {}
    if "brightness" in value:
        out["Brightness"] = value["brightness"]
    if "sharpness" in value:
        out["Sharpness"] = value["sharpness"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageQuality:
    out: ImageQuality = {}  # type: ignore[typeddict-item]
    if "Brightness" in data:
        out["brightness"] = data["Brightness"]
    if "Sharpness" in data:
        out["sharpness"] = data["Sharpness"]
    return out
