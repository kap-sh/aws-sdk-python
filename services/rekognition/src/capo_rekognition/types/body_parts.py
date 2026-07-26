"""Generated from Smithy shape ``com.amazonaws.rekognition#BodyParts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.protective_equipment_body_part

BodyParts: TypeAlias = list[
    "capo_rekognition.types.protective_equipment_body_part.ProtectiveEquipmentBodyPart"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BodyParts) -> list:
    import capo_rekognition.types.protective_equipment_body_part

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.protective_equipment_body_part.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BodyParts:
    import capo_rekognition.types.protective_equipment_body_part

    out: BodyParts = []
    for item in data:
        out.append(
            capo_rekognition.types.protective_equipment_body_part.deserialize_aws_json_1_1(
                item
            )
        )
    return out
