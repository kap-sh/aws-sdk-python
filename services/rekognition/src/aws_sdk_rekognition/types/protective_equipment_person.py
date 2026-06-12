"""Generated from Smithy shape ``com.amazonaws.rekognition#ProtectiveEquipmentPerson``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.body_parts
    import aws_sdk_rekognition.types.bounding_box
    import aws_sdk_rekognition.types.percent
    import aws_sdk_rekognition.types.u_integer


class ProtectiveEquipmentPerson(TypedDict):
    body_parts: NotRequired["aws_sdk_rekognition.types.body_parts.BodyParts"]
    """<p>An array of body parts detected on a person's body (including body parts without PPE). </p>"""
    bounding_box: NotRequired["aws_sdk_rekognition.types.bounding_box.BoundingBox"]
    """<p>A bounding box around the detected person.</p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>The confidence that Amazon Rekognition has that the bounding box contains a person.</p>"""
    id: NotRequired["aws_sdk_rekognition.types.u_integer.UInteger"]
    """<p>The identifier for the detected person. The identifier is only unique for a single call to <code>DetectProtectiveEquipment</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectiveEquipmentPerson) -> dict:
    out: dict = {}
    if "body_parts" in value:
        import aws_sdk_rekognition.types.body_parts

        out["BodyParts"] = aws_sdk_rekognition.types.body_parts.serialize_aws_json_1_1(
            value["body_parts"]
        )
    if "bounding_box" in value:
        import aws_sdk_rekognition.types.bounding_box

        out["BoundingBox"] = (
            aws_sdk_rekognition.types.bounding_box.serialize_aws_json_1_1(
                value["bounding_box"]
            )
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtectiveEquipmentPerson:
    out: ProtectiveEquipmentPerson = {}  # type: ignore[typeddict-item]
    if "BodyParts" in data:
        import aws_sdk_rekognition.types.body_parts

        out["body_parts"] = (
            aws_sdk_rekognition.types.body_parts.deserialize_aws_json_1_1(
                data["BodyParts"]
            )
        )
    if "BoundingBox" in data:
        import aws_sdk_rekognition.types.bounding_box

        out["bounding_box"] = (
            aws_sdk_rekognition.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
