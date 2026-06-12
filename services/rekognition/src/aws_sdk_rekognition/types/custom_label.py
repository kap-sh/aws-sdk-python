"""Generated from Smithy shape ``com.amazonaws.rekognition#CustomLabel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.geometry
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.string


class CustomLabel(TypedDict):
    name: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The name of the custom label.</p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>The confidence that the model has in the detection of the custom label. The range is 0-100. A higher value indicates a higher confidence.</p>"""
    geometry: NotRequired["aws_sdk_rekognition.types.geometry.Geometry"]
    """<p>The location of the detected object on the image that corresponds to the custom label. Includes an axis aligned coarse bounding box surrounding the object and a finer grain polygon for more accurate spatial information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomLabel) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "geometry" in value:
        import aws_sdk_rekognition.types.geometry

        out["Geometry"] = aws_sdk_rekognition.types.geometry.serialize_aws_json_1_1(
            value["geometry"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomLabel:
    out: CustomLabel = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Geometry" in data:
        import aws_sdk_rekognition.types.geometry

        out["geometry"] = aws_sdk_rekognition.types.geometry.deserialize_aws_json_1_1(
            data["Geometry"]
        )
    return out
