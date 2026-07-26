"""Generated from Smithy shape ``com.amazonaws.rekognition#ProtectiveEquipmentBodyPart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.body_part
    import capo_rekognition.types.equipment_detections
    import capo_rekognition.types.percent


class ProtectiveEquipmentBodyPart(TypedDict, closed=True):
    name: NotRequired["capo_rekognition.types.body_part.BodyPart"]
    """<p>The detected body part.</p>"""
    confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p>The confidence that Amazon Rekognition has in the detection accuracy of the detected body part. </p>"""
    equipment_detections: NotRequired[
        "capo_rekognition.types.equipment_detections.EquipmentDetections"
    ]
    """<p>An array of Personal Protective Equipment items detected around a body part.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectiveEquipmentBodyPart) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_rekognition.types.body_part

        out["Name"] = capo_rekognition.types.body_part.serialize_aws_json_1_1(
            value["name"]
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "equipment_detections" in value:
        import capo_rekognition.types.equipment_detections

        out["EquipmentDetections"] = (
            capo_rekognition.types.equipment_detections.serialize_aws_json_1_1(
                value["equipment_detections"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtectiveEquipmentBodyPart:
    out: ProtectiveEquipmentBodyPart = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import capo_rekognition.types.body_part

        out["name"] = capo_rekognition.types.body_part.deserialize_aws_json_1_1(
            data["Name"]
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "EquipmentDetections" in data:
        import capo_rekognition.types.equipment_detections

        out["equipment_detections"] = (
            capo_rekognition.types.equipment_detections.deserialize_aws_json_1_1(
                data["EquipmentDetections"]
            )
        )
    return out
