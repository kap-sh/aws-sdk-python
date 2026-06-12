"""Generated from Smithy shape ``com.amazonaws.rekognition#ProtectiveEquipmentPersonIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.u_integer

ProtectiveEquipmentPersonIds: TypeAlias = list[
    "aws_sdk_rekognition.types.u_integer.UInteger"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectiveEquipmentPersonIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProtectiveEquipmentPersonIds:
    return list(data)
