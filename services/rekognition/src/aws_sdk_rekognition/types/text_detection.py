"""Generated from Smithy shape ``com.amazonaws.rekognition#TextDetection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.geometry
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.string
    import aws_sdk_rekognition.types.text_types
    import aws_sdk_rekognition.types.u_integer


class TextDetection(TypedDict):
    detected_text: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>The word or line of text recognized by Amazon Rekognition. </p>"""
    type: NotRequired["aws_sdk_rekognition.types.text_types.TextTypes"]
    """<p>The type of text that was detected.</p>"""
    id: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p>The identifier for the detected text. The identifier is only unique for a single call to <code>DetectText</code>. </p>"""
    parent_id: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p>The Parent identifier for the detected text identified by the value of <code>ID</code>. If the type of detected text is <code>LINE</code>, the value of <code>ParentId</code> is <code>Null</code>. </p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>The confidence that Amazon Rekognition has in the accuracy of the detected text and the accuracy of the geometry points around the detected text.</p>"""
    geometry: NotRequired["aws_sdk_rekognition.types.geometry.Geometry"]
    """<p>The location of the detected text on the image. Includes an axis aligned coarse bounding box surrounding the text and a finer grain polygon for more accurate spatial information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextDetection) -> dict:
    out: dict = {}
    if "detected_text" in value:
        out["DetectedText"] = value["detected_text"]
    if "type" in value:
        import aws_sdk_rekognition.types.text_types

        out["Type"] = aws_sdk_rekognition.types.text_types.serialize_aws_json_1_1(
            value["type"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "parent_id" in value:
        out["ParentId"] = value["parent_id"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "geometry" in value:
        import aws_sdk_rekognition.types.geometry

        out["Geometry"] = aws_sdk_rekognition.types.geometry.serialize_aws_json_1_1(
            value["geometry"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TextDetection:
    out: TextDetection = {}  # type: ignore[typeddict-item]
    if "DetectedText" in data:
        out["detected_text"] = data["DetectedText"]
    if "Type" in data:
        import aws_sdk_rekognition.types.text_types

        out["type"] = aws_sdk_rekognition.types.text_types.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "ParentId" in data:
        out["parent_id"] = data["ParentId"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Geometry" in data:
        import aws_sdk_rekognition.types.geometry

        out["geometry"] = aws_sdk_rekognition.types.geometry.deserialize_aws_json_1_1(
            data["Geometry"]
        )
    return out
