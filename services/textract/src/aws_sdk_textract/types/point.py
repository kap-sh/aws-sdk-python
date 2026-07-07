"""Generated from Smithy shape ``com.amazonaws.textract#Point``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.float


class Point(TypedDict, closed=True):
    x: "aws_sdk_textract.types.float.Float"
    """<p>The value of the X coordinate for a point on a <code>Polygon</code>.</p>"""
    y: "aws_sdk_textract.types.float.Float"
    """<p>The value of the Y coordinate for a point on a <code>Polygon</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Point) -> dict:
    out: dict = {}
    out["X"] = value.get("x", 0)
    out["Y"] = value.get("y", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> Point:
    out: Point = {}  # type: ignore[typeddict-item]
    if "X" in data:
        out["x"] = data["X"]
    else:
        out["x"] = 0
    if "Y" in data:
        out["y"] = data["Y"]
    else:
        out["y"] = 0
    return out
