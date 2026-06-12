"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatIntelSetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

ThreatIntelSetStatus: TypeAlias = Literal[
    "INACTIVE",
    "ACTIVATING",
    "ACTIVE",
    "DEACTIVATING",
    "ERROR",
    "DELETE_PENDING",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INACTIVE",
        "ACTIVATING",
        "ACTIVE",
        "DEACTIVATING",
        "ERROR",
        "DELETE_PENDING",
        "DELETED",
    )
)


def serialize_json(value: ThreatIntelSetStatus) -> str:
    return value


def deserialize_json(data: str) -> ThreatIntelSetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThreatIntelSetStatus value: {data!r}")
    return cast(ThreatIntelSetStatus, data)
