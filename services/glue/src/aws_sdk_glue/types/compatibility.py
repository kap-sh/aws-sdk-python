"""Generated from Smithy shape ``com.amazonaws.glue#Compatibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

Compatibility: TypeAlias = Literal[
    "NONE",
    "DISABLED",
    "BACKWARD",
    "BACKWARD_ALL",
    "FORWARD",
    "FORWARD_ALL",
    "FULL",
    "FULL_ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "DISABLED",
        "BACKWARD",
        "BACKWARD_ALL",
        "FORWARD",
        "FORWARD_ALL",
        "FULL",
        "FULL_ALL",
    )
)


def serialize_aws_json_1_1(value: Compatibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Compatibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Compatibility value: {data!r}")
    return cast(Compatibility, data)
