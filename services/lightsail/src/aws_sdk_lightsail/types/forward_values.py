"""Generated from Smithy shape ``com.amazonaws.lightsail#ForwardValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

ForwardValues: TypeAlias = Literal[
    "none",
    "allow-list",
    "all",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "allow-list",
        "all",
    )
)


def serialize_aws_json_1_1(value: ForwardValues) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ForwardValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ForwardValues value: {data!r}")
    return cast(ForwardValues, data)
