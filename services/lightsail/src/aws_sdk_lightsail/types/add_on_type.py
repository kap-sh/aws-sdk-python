"""Generated from Smithy shape ``com.amazonaws.lightsail#AddOnType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

AddOnType: TypeAlias = Literal[
    "AutoSnapshot",
    "StopInstanceOnIdle",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AutoSnapshot",
        "StopInstanceOnIdle",
    )
)


def serialize_aws_json_1_1(value: AddOnType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AddOnType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AddOnType value: {data!r}")
    return cast(AddOnType, data)
