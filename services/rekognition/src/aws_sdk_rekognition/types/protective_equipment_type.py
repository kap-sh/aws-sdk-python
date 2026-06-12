"""Generated from Smithy shape ``com.amazonaws.rekognition#ProtectiveEquipmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

ProtectiveEquipmentType: TypeAlias = Literal[
    "FACE_COVER",
    "HAND_COVER",
    "HEAD_COVER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FACE_COVER",
        "HAND_COVER",
        "HEAD_COVER",
    )
)


def serialize_aws_json_1_1(value: ProtectiveEquipmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProtectiveEquipmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProtectiveEquipmentType value: {data!r}")
    return cast(ProtectiveEquipmentType, data)
