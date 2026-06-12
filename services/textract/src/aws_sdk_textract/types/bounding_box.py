"""Generated from Smithy shape ``com.amazonaws.textract#BoundingBox``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.float


class BoundingBox(TypedDict):
    width: "aws_sdk_textract.types.float.Float"
    """<p>The width of the bounding box as a ratio of the overall document page width.</p>"""
    height: "aws_sdk_textract.types.float.Float"
    """<p>The height of the bounding box as a ratio of the overall document page height.</p>"""
    left: "aws_sdk_textract.types.float.Float"
    """<p>The left coordinate of the bounding box as a ratio of overall document page width.</p>"""
    top: "aws_sdk_textract.types.float.Float"
    """<p>The top coordinate of the bounding box as a ratio of overall document page height.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BoundingBox) -> dict:
    out: dict = {}
    out["Width"] = value.get("width", 0)
    out["Height"] = value.get("height", 0)
    out["Left"] = value.get("left", 0)
    out["Top"] = value.get("top", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> BoundingBox:
    out: BoundingBox = {}  # type: ignore[typeddict-item]
    if "Width" in data:
        out["width"] = data["Width"]
    else:
        out["width"] = 0
    if "Height" in data:
        out["height"] = data["Height"]
    else:
        out["height"] = 0
    if "Left" in data:
        out["left"] = data["Left"]
    else:
        out["left"] = 0
    if "Top" in data:
        out["top"] = data["Top"]
    else:
        out["top"] = 0
    return out
