"""Generated from Smithy shape ``com.amazonaws.connect#ContactState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ContactState: TypeAlias = Literal[
    "INCOMING",
    "PENDING",
    "CONNECTING",
    "CONNECTED",
    "CONNECTED_ONHOLD",
    "MISSED",
    "ERROR",
    "ENDED",
    "REJECTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCOMING",
        "PENDING",
        "CONNECTING",
        "CONNECTED",
        "CONNECTED_ONHOLD",
        "MISSED",
        "ERROR",
        "ENDED",
        "REJECTED",
    )
)


def serialize_json(value: ContactState) -> str:
    return value


def deserialize_json(data: str) -> ContactState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactState value: {data!r}")
    return cast(ContactState, data)
