"""Generated from Smithy shape ``com.amazonaws.textract#Geometry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.angle
    import aws_sdk_textract.types.bounding_box
    import aws_sdk_textract.types.polygon


class Geometry(TypedDict):
    bounding_box: NotRequired["aws_sdk_textract.types.bounding_box.BoundingBox"]
    """<p>An axis-aligned coarse representation of the location of the recognized item on the document page.</p>"""
    polygon: NotRequired["aws_sdk_textract.types.polygon.Polygon"]
    """<p>Within the bounding box, a fine-grained polygon around the recognized item.</p>"""
    rotation_angle: NotRequired["aws_sdk_textract.types.angle.Angle"]
    """<p>Provides a numerical value corresponding to the rotation of the text.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Geometry) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import aws_sdk_textract.types.bounding_box

        out["BoundingBox"] = aws_sdk_textract.types.bounding_box.serialize_aws_json_1_1(
            value["bounding_box"]
        )
    if "polygon" in value:
        import aws_sdk_textract.types.polygon

        out["Polygon"] = aws_sdk_textract.types.polygon.serialize_aws_json_1_1(
            value["polygon"]
        )
    if "rotation_angle" in value:
        out["RotationAngle"] = value["rotation_angle"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Geometry:
    out: Geometry = {}  # type: ignore[typeddict-item]
    if "BoundingBox" in data:
        import aws_sdk_textract.types.bounding_box

        out["bounding_box"] = (
            aws_sdk_textract.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if "Polygon" in data:
        import aws_sdk_textract.types.polygon

        out["polygon"] = aws_sdk_textract.types.polygon.deserialize_aws_json_1_1(
            data["Polygon"]
        )
    if "RotationAngle" in data:
        out["rotation_angle"] = data["RotationAngle"]
    return out
