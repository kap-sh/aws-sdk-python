"""Generated from Smithy shape ``com.amazonaws.auditmanager#EvidenceFinderBackfillStatus``."""

from typing import Literal, TypeAlias, cast

EvidenceFinderBackfillStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EvidenceFinderBackfillStatus) -> str:
    return value


def deserialize_json(data: str) -> EvidenceFinderBackfillStatus:
    return cast(EvidenceFinderBackfillStatus, data)
