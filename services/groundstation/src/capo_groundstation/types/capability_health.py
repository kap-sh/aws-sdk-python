"""Generated from Smithy shape ``com.amazonaws.groundstation#CapabilityHealth``."""

from typing import Literal, TypeAlias, cast

CapabilityHealth: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityHealth) -> str:
    return value


def deserialize_json(data: str) -> CapabilityHealth:
    return cast(CapabilityHealth, data)
