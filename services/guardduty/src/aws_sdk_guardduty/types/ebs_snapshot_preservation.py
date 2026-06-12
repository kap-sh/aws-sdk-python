"""Generated from Smithy shape ``com.amazonaws.guardduty#EbsSnapshotPreservation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

EbsSnapshotPreservation: TypeAlias = Literal[
    "NO_RETENTION",
    "RETENTION_WITH_FINDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_RETENTION",
        "RETENTION_WITH_FINDING",
    )
)


def serialize_json(value: EbsSnapshotPreservation) -> str:
    return value


def deserialize_json(data: str) -> EbsSnapshotPreservation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EbsSnapshotPreservation value: {data!r}")
    return cast(EbsSnapshotPreservation, data)
