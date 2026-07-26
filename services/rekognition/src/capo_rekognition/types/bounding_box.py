"""Generated from Smithy shape ``com.amazonaws.rekognition#BoundingBox``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.float


class BoundingBox(TypedDict, closed=True):
    width: NotRequired["capo_rekognition.types.float.Float"]
    """<p>Width of the bounding box as a ratio of the overall image width.</p>"""
    height: NotRequired["capo_rekognition.types.float.Float"]
    """<p>Height of the bounding box as a ratio of the overall image height.</p>"""
    left: NotRequired["capo_rekognition.types.float.Float"]
    """<p>Left coordinate of the bounding box as a ratio of overall image width.</p>"""
    top: NotRequired["capo_rekognition.types.float.Float"]
    """<p>Top coordinate of the bounding box as a ratio of overall image height.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BoundingBox) -> dict:
    out: dict = {}
    if "width" in value:
        out["Width"] = value["width"]
    if "height" in value:
        out["Height"] = value["height"]
    if "left" in value:
        out["Left"] = value["left"]
    if "top" in value:
        out["Top"] = value["top"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BoundingBox:
    out: BoundingBox = {}  # type: ignore[typeddict-item]
    if "Width" in data:
        out["width"] = data["Width"]
    if "Height" in data:
        out["height"] = data["Height"]
    if "Left" in data:
        out["left"] = data["Left"]
    if "Top" in data:
        out["top"] = data["Top"]
    return out
