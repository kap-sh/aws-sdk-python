"""Generated from Smithy shape ``com.amazonaws.lightsail#DiskState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

DiskState: TypeAlias = Literal[
    "pending",
    "error",
    "available",
    "in-use",
    "unknown",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "error",
        "available",
        "in-use",
        "unknown",
    )
)


def serialize_aws_json_1_1(value: DiskState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DiskState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DiskState value: {data!r}")
    return cast(DiskState, data)
