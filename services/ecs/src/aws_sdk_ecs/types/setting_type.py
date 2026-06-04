"""Generated from Smithy shape ``com.amazonaws.ecs#SettingType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

SettingType: TypeAlias = Literal[
    "user",
    "aws_managed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "user",
        "aws_managed",
    )
)


def serialize_aws_json_1_1(value: SettingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SettingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SettingType value: {data!r}")
    return cast(SettingType, data)
