"""Generated from Smithy shape ``com.amazonaws.directconnect#LagState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

LagState: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: LagState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LagState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LagState value: {data!r}")
    return cast(LagState, data)
