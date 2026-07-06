"""Generated from Smithy shape ``com.amazonaws.rekognition#Geometry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.bounding_box
    import aws_sdk_rekognition.types.polygon


class Geometry(TypedDict, closed=True):
    bounding_box: NotRequired["aws_sdk_rekognition.types.bounding_box.BoundingBox"]
    """<p>An axis-aligned coarse representation of the detected item's location on the image.</p>"""
    polygon: NotRequired["aws_sdk_rekognition.types.polygon.Polygon"]
    """<p>Within the bounding box, a fine-grained polygon around the detected item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Geometry) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import aws_sdk_rekognition.types.bounding_box

        out["BoundingBox"] = (
            aws_sdk_rekognition.types.bounding_box.serialize_aws_json_1_1(
                value["bounding_box"]
            )
        )
    if "polygon" in value:
        import aws_sdk_rekognition.types.polygon

        out["Polygon"] = aws_sdk_rekognition.types.polygon.serialize_aws_json_1_1(
            value["polygon"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Geometry:
    out: Geometry = {}  # type: ignore[typeddict-item]
    if "BoundingBox" in data:
        import aws_sdk_rekognition.types.bounding_box

        out["bounding_box"] = (
            aws_sdk_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if "Polygon" in data:
        import aws_sdk_rekognition.types.polygon

        out["polygon"] = aws_sdk_rekognition.types.polygon.deserialize_aws_json_1_1(
            data["Polygon"]
        )
    return out
