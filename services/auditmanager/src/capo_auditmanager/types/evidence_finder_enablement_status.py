"""Generated from Smithy shape ``com.amazonaws.auditmanager#EvidenceFinderEnablementStatus``."""

from typing import Literal, TypeAlias, cast

EvidenceFinderEnablementStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLE_IN_PROGRESS",
    "DISABLE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvidenceFinderEnablementStatus) -> str:
    return value


def deserialize_json(data: str) -> EvidenceFinderEnablementStatus:
    return cast(EvidenceFinderEnablementStatus, data)
