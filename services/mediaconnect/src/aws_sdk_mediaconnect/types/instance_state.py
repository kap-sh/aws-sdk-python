"""Generated from Smithy shape ``com.amazonaws.mediaconnect#InstanceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

InstanceState: TypeAlias = Literal[
    "REGISTERING",
    "ACTIVE",
    "DEREGISTERING",
    "DEREGISTERED",
    "REGISTRATION_ERROR",
    "DEREGISTRATION_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGISTERING",
        "ACTIVE",
        "DEREGISTERING",
        "DEREGISTERED",
        "REGISTRATION_ERROR",
        "DEREGISTRATION_ERROR",
    )
)


def serialize_json(value: InstanceState) -> str:
    return value


def deserialize_json(data: str) -> InstanceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceState value: {data!r}")
    return cast(InstanceState, data)
