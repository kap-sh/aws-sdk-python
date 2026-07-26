"""Generated from Smithy shape ``com.amazonaws.rekognition#ProtectiveEquipmentType``."""

from typing import Literal, TypeAlias, cast

ProtectiveEquipmentType: TypeAlias = Literal[
    "FACE_COVER",
    "HAND_COVER",
    "HEAD_COVER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectiveEquipmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProtectiveEquipmentType:
    return cast(ProtectiveEquipmentType, data)
