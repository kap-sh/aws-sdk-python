"""Generated from Smithy shape ``com.amazonaws.comprehend#BoundingBox``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.float


class BoundingBox(TypedDict, closed=True):
    height: NotRequired["aws_sdk_comprehend.types.float.Float"]
    """<p>The height of the bounding box as a ratio of the overall document page height.</p>"""
    left: NotRequired["aws_sdk_comprehend.types.float.Float"]
    """<p>The left coordinate of the bounding box as a ratio of overall document page width.</p>"""
    top: NotRequired["aws_sdk_comprehend.types.float.Float"]
    """<p>The top coordinate of the bounding box as a ratio of overall document page height.</p>"""
    width: NotRequired["aws_sdk_comprehend.types.float.Float"]
    """<p>The width of the bounding box as a ratio of the overall document page width.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BoundingBox) -> dict:
    out: dict = {}
    if "height" in value:
        out["Height"] = value["height"]
    if "left" in value:
        out["Left"] = value["left"]
    if "top" in value:
        out["Top"] = value["top"]
    if "width" in value:
        out["Width"] = value["width"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BoundingBox:
    out: BoundingBox = {}  # type: ignore[typeddict-item]
    if "Height" in data:
        out["height"] = data["Height"]
    if "Left" in data:
        out["left"] = data["Left"]
    if "Top" in data:
        out["top"] = data["Top"]
    if "Width" in data:
        out["width"] = data["Width"]
    return out
