"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectLabelsImageQuality``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.float


class DetectLabelsImageQuality(TypedDict):
    brightness: NotRequired["aws_sdk_rekognition.types.float.Float"]
    """<p>The brightness of an image provided for label detection.</p>"""
    sharpness: NotRequired["aws_sdk_rekognition.types.float.Float"]
    """<p>The sharpness of an image provided for label detection.</p>"""
    contrast: NotRequired["aws_sdk_rekognition.types.float.Float"]
    """<p>The contrast of an image provided for label detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectLabelsImageQuality) -> dict:
    out: dict = {}
    if "brightness" in value:
        out["Brightness"] = value["brightness"]
    if "sharpness" in value:
        out["Sharpness"] = value["sharpness"]
    if "contrast" in value:
        out["Contrast"] = value["contrast"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectLabelsImageQuality:
    out: DetectLabelsImageQuality = {}  # type: ignore[typeddict-item]
    if "Brightness" in data:
        out["brightness"] = data["Brightness"]
    if "Sharpness" in data:
        out["sharpness"] = data["Sharpness"]
    if "Contrast" in data:
        out["contrast"] = data["Contrast"]
    return out
