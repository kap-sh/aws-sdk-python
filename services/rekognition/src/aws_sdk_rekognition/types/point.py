"""Generated from Smithy shape ``com.amazonaws.rekognition#Point``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.float


class Point(TypedDict):
    x: NotRequired["aws_sdk_rekognition.types.float.Float"]
    """<p>The value of the X coordinate for a point on a <code>Polygon</code>.</p>"""
    y: NotRequired["aws_sdk_rekognition.types.float.Float"]
    """<p>The value of the Y coordinate for a point on a <code>Polygon</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Point) -> dict:
    out: dict = {}
    if "x" in value:
        out["X"] = value["x"]
    if "y" in value:
        out["Y"] = value["y"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Point:
    out: Point = {}  # type: ignore[typeddict-item]
    if "X" in data:
        out["x"] = data["X"]
    if "Y" in data:
        out["y"] = data["Y"]
    return out
