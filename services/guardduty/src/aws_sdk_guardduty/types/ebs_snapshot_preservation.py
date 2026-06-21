"""Generated from Smithy shape ``com.amazonaws.guardduty#EbsSnapshotPreservation``."""

from typing import Literal, TypeAlias, cast

EbsSnapshotPreservation: TypeAlias = Literal[
    "NO_RETENTION",
    "RETENTION_WITH_FINDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: EbsSnapshotPreservation) -> str:
    return value


def deserialize_json(data: str) -> EbsSnapshotPreservation:
    return cast(EbsSnapshotPreservation, data)
