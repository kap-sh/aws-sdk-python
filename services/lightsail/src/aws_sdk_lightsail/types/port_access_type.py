"""Generated from Smithy shape ``com.amazonaws.lightsail#PortAccessType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

PortAccessType: TypeAlias = Literal[
    "Public",
    "Private",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Public",
        "Private",
    )
)


def serialize_aws_json_1_1(value: PortAccessType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PortAccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PortAccessType value: {data!r}")
    return cast(PortAccessType, data)
