"""Generated from Smithy shape ``com.amazonaws.rekognition#EquipmentDetections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.equipment_detection

EquipmentDetections: TypeAlias = list[
    "capo_rekognition.types.equipment_detection.EquipmentDetection"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EquipmentDetections) -> list:
    import capo_rekognition.types.equipment_detection

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.equipment_detection.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EquipmentDetections:
    import capo_rekognition.types.equipment_detection

    out: EquipmentDetections = []
    for item in data:
        out.append(
            capo_rekognition.types.equipment_detection.deserialize_aws_json_1_1(item)
        )
    return out
