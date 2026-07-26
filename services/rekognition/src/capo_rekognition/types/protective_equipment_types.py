"""Generated from Smithy shape ``com.amazonaws.rekognition#ProtectiveEquipmentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.protective_equipment_type

ProtectiveEquipmentTypes: TypeAlias = list[
    "capo_rekognition.types.protective_equipment_type.ProtectiveEquipmentType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectiveEquipmentTypes) -> list:
    import capo_rekognition.types.protective_equipment_type

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.protective_equipment_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProtectiveEquipmentTypes:
    import capo_rekognition.types.protective_equipment_type

    out: ProtectiveEquipmentTypes = []
    for item in data:
        out.append(
            capo_rekognition.types.protective_equipment_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
