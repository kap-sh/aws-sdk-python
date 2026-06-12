"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#EntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotthingsgraph.errors import DeserializationError

EntityType: TypeAlias = Literal[
    "DEVICE",
    "SERVICE",
    "DEVICE_MODEL",
    "CAPABILITY",
    "STATE",
    "ACTION",
    "EVENT",
    "PROPERTY",
    "MAPPING",
    "ENUM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEVICE",
        "SERVICE",
        "DEVICE_MODEL",
        "CAPABILITY",
        "STATE",
        "ACTION",
        "EVENT",
        "PROPERTY",
        "MAPPING",
        "ENUM",
    )
)


def serialize_aws_json_1_1(value: EntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityType value: {data!r}")
    return cast(EntityType, data)
