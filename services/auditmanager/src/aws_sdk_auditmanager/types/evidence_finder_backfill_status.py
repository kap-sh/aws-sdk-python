"""Generated from Smithy shape ``com.amazonaws.auditmanager#EvidenceFinderBackfillStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

EvidenceFinderBackfillStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_STARTED",
        "IN_PROGRESS",
        "COMPLETED",
    )
)


def serialize_json(value: EvidenceFinderBackfillStatus) -> str:
    return value


def deserialize_json(data: str) -> EvidenceFinderBackfillStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvidenceFinderBackfillStatus value: {data!r}"
        )
    return cast(EvidenceFinderBackfillStatus, data)
