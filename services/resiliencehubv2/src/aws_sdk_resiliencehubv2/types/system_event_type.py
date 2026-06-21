"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemEventType``."""

from typing import Literal, TypeAlias, cast

SystemEventType: TypeAlias = Literal[
    "SYSTEM_CREATED",
    "SYSTEM_DELETED",
    "SYSTEM_USER_JOURNEY_CREATED",
    "SYSTEM_USER_JOURNEY_UPDATED",
    "SYSTEM_USER_JOURNEY_DELETED",
    "SYSTEM_SERVICE_ASSOCIATED",
    "SYSTEM_SERVICE_DISASSOCIATED",
    "SYSTEM_POLICY_ASSOCIATED",
    "SYSTEM_POLICY_DISASSOCIATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SystemEventType) -> str:
    return value


def deserialize_json(data: str) -> SystemEventType:
    return cast(SystemEventType, data)
