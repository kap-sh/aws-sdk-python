"""Generated from Smithy shape ``com.amazonaws.mediaconnect#InstanceState``."""

from typing import Literal, TypeAlias, cast

InstanceState: TypeAlias = Literal[
    "REGISTERING",
    "ACTIVE",
    "DEREGISTERING",
    "DEREGISTERED",
    "REGISTRATION_ERROR",
    "DEREGISTRATION_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceState) -> str:
    return value


def deserialize_json(data: str) -> InstanceState:
    return cast(InstanceState, data)
