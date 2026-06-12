"""Generated from Smithy shape ``com.amazonaws.networkmanager#PeeringState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

PeeringState: TypeAlias = Literal[
    "CREATING",
    "FAILED",
    "AVAILABLE",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "FAILED",
        "AVAILABLE",
        "DELETING",
    )
)


def serialize_json(value: PeeringState) -> str:
    return value


def deserialize_json(data: str) -> PeeringState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PeeringState value: {data!r}")
    return cast(PeeringState, data)
