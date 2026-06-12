"""Generated from Smithy shape ``com.amazonaws.directconnect#InterconnectState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

InterconnectState: TypeAlias = Literal[
    "requested",
    "pending",
    "available",
    "down",
    "deleting",
    "deleted",
    "unknown",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "requested",
        "pending",
        "available",
        "down",
        "deleting",
        "deleted",
        "unknown",
    )
)


def serialize_aws_json_1_1(value: InterconnectState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InterconnectState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InterconnectState value: {data!r}")
    return cast(InterconnectState, data)
