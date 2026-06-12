"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatEntitySetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

ThreatEntitySetStatus: TypeAlias = Literal[
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


def serialize_json(value: ThreatEntitySetStatus) -> str:
    return value


def deserialize_json(data: str) -> ThreatEntitySetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThreatEntitySetStatus value: {data!r}")
    return cast(ThreatEntitySetStatus, data)
