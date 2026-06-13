"""Generated from Smithy shape ``com.amazonaws.groundstation#CapabilityHealthReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "NO_REGISTERED_AGENT",
        "INVALID_IP_OWNERSHIP",
        "NOT_AUTHORIZED_TO_CREATE_SLR",
        "UNVERIFIED_IP_OWNERSHIP",
        "INITIALIZING_DATAPLANE",
        "DATAPLANE_FAILURE",
        "HEALTHY",
    )
)


def serialize_json(value: CapabilityHealthReason) -> str:
    return value


def deserialize_json(data: str) -> CapabilityHealthReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapabilityHealthReason value: {data!r}")
    return cast(CapabilityHealthReason, data)
