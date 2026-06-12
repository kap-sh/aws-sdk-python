"""Generated from Smithy shape ``com.amazonaws.rekognition#ProtectiveEquipmentBodyPart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.body_part
    import aws_sdk_rekognition.types.equipment_detections
    import aws_sdk_rekognition.types.percent


class ProtectiveEquipmentBodyPart(TypedDict):
    name: NotRequired["aws_sdk_rekognition.types.body_part.BodyPart"]
    """<p>The detected body part.</p>"""
    confidence: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>The confidence that Amazon Rekognition has in the detection accuracy of the detected body part. </p>"""
    equipment_detections: NotRequired[
        "aws_sdk_rekognition.types.equipment_detections.EquipmentDetections"
    ]
    """<p>An array of Personal Protective Equipment items detected around a body part.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectiveEquipmentBodyPart) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_rekognition.types.body_part

        out["Name"] = aws_sdk_rekognition.types.body_part.serialize_aws_json_1_1(
            value["name"]
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "equipment_detections" in value:
        import aws_sdk_rekognition.types.equipment_detections

        out["EquipmentDetections"] = (
            aws_sdk_rekognition.types.equipment_detections.serialize_aws_json_1_1(
                value["equipment_detections"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtectiveEquipmentBodyPart:
    out: ProtectiveEquipmentBodyPart = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_rekognition.types.body_part

        out["name"] = aws_sdk_rekognition.types.body_part.deserialize_aws_json_1_1(
            data["Name"]
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "EquipmentDetections" in data:
        import aws_sdk_rekognition.types.equipment_detections

        out["equipment_detections"] = (
            aws_sdk_rekognition.types.equipment_detections.deserialize_aws_json_1_1(
                data["EquipmentDetections"]
            )
        )
    return out
