"""Generated from Smithy shape ``com.amazonaws.lightsail#PortState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

PortState: TypeAlias = Literal[
    "open",
    "closed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "open",
        "closed",
    )
)


def serialize_aws_json_1_1(value: PortState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PortState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PortState value: {data!r}")
    return cast(PortState, data)
