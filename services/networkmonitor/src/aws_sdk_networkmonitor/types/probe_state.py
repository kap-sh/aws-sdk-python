"""Generated from Smithy shape ``com.amazonaws.networkmonitor#ProbeState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmonitor.errors import DeserializationError

ProbeState: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "INACTIVE",
    "ERROR",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACTIVE",
        "INACTIVE",
        "ERROR",
        "DELETING",
        "DELETED",
    )
)


def serialize_json(value: ProbeState) -> str:
    return value


def deserialize_json(data: str) -> ProbeState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProbeState value: {data!r}")
    return cast(ProbeState, data)
