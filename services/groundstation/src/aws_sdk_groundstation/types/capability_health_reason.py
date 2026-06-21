"""Generated from Smithy shape ``com.amazonaws.groundstation#CapabilityHealthReason``."""

from typing import Literal, TypeAlias, cast

CapabilityHealthReason: TypeAlias = Literal[
    "NO_REGISTERED_AGENT",
    "INVALID_IP_OWNERSHIP",
    "NOT_AUTHORIZED_TO_CREATE_SLR",
    "UNVERIFIED_IP_OWNERSHIP",
    "INITIALIZING_DATAPLANE",
    "DATAPLANE_FAILURE",
    "HEALTHY",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityHealthReason) -> str:
    return value


def deserialize_json(data: str) -> CapabilityHealthReason:
    return cast(CapabilityHealthReason, data)
