"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

ConnectionState: TypeAlias = Literal[
    "CONNECTED",
    "DISCONNECTED",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECTED",
        "DISCONNECTED",
        "UNKNOWN",
    )
)


def serialize_aws_json_1_1(value: ConnectionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionState value: {data!r}")
    return cast(ConnectionState, data)
