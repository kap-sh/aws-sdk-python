"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatEntitySetStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ThreatEntitySetStatus) -> str:
    return value


def deserialize_json(data: str) -> ThreatEntitySetStatus:
    return cast(ThreatEntitySetStatus, data)
