"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GatewayState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

GatewayState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "ERROR",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "ERROR",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: GatewayState) -> str:
    return value


def deserialize_json(data: str) -> GatewayState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GatewayState value: {data!r}")
    return cast(GatewayState, data)
