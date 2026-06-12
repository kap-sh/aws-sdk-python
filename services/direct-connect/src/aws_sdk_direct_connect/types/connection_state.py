"""Generated from Smithy shape ``com.amazonaws.directconnect#ConnectionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

ConnectionState: TypeAlias = Literal[
    "ordering",
    "requested",
    "pending",
    "available",
    "down",
    "deleting",
    "deleted",
    "rejected",
    "unknown",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ordering",
        "requested",
        "pending",
        "available",
        "down",
        "deleting",
        "deleted",
        "rejected",
        "unknown",
    )
)


def serialize_aws_json_1_1(value: ConnectionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionState value: {data!r}")
    return cast(ConnectionState, data)
