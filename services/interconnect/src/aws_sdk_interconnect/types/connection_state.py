"""Generated from Smithy shape ``com.amazonaws.interconnect#ConnectionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_interconnect.errors import DeserializationError

ConnectionState: TypeAlias = Literal[
    "available",
    "requested",
    "pending",
    "down",
    "deleting",
    "deleted",
    "failed",
    "updating",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "requested",
        "pending",
        "down",
        "deleting",
        "deleted",
        "failed",
        "updating",
    )
)


def serialize_aws_json_1_0(value: ConnectionState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConnectionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionState value: {data!r}")
    return cast(ConnectionState, data)
