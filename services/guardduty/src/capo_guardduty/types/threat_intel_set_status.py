"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatIntelSetStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ThreatIntelSetStatus) -> str:
    return value


def deserialize_json(data: str) -> ThreatIntelSetStatus:
    return cast(ThreatIntelSetStatus, data)
