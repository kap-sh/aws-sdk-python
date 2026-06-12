"""Generated from Smithy shape ``com.amazonaws.lightsail#PortInfoSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

PortInfoSourceType: TypeAlias = Literal[
    "DEFAULT",
    "INSTANCE",
    "NONE",
    "CLOSED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "INSTANCE",
        "NONE",
        "CLOSED",
    )
)


def serialize_aws_json_1_1(value: PortInfoSourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PortInfoSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PortInfoSourceType value: {data!r}")
    return cast(PortInfoSourceType, data)
