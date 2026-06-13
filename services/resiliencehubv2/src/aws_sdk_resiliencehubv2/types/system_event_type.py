"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "SYSTEM_CREATED",
        "SYSTEM_DELETED",
        "SYSTEM_USER_JOURNEY_CREATED",
        "SYSTEM_USER_JOURNEY_UPDATED",
        "SYSTEM_USER_JOURNEY_DELETED",
        "SYSTEM_SERVICE_ASSOCIATED",
        "SYSTEM_SERVICE_DISASSOCIATED",
        "SYSTEM_POLICY_ASSOCIATED",
        "SYSTEM_POLICY_DISASSOCIATED",
    )
)


def serialize_json(value: SystemEventType) -> str:
    return value


def deserialize_json(data: str) -> SystemEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SystemEventType value: {data!r}")
    return cast(SystemEventType, data)
