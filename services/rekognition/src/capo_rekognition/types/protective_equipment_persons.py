"""Generated from Smithy shape ``com.amazonaws.rekognition#ProtectiveEquipmentPersons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.protective_equipment_person

ProtectiveEquipmentPersons: TypeAlias = list[
    "capo_rekognition.types.protective_equipment_person.ProtectiveEquipmentPerson"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectiveEquipmentPersons) -> list:
    import capo_rekognition.types.protective_equipment_person

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.protective_equipment_person.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProtectiveEquipmentPersons:
    import capo_rekognition.types.protective_equipment_person

    out: ProtectiveEquipmentPersons = []
    for item in data:
        out.append(
            capo_rekognition.types.protective_equipment_person.deserialize_aws_json_1_1(
                item
            )
        )
    return out
