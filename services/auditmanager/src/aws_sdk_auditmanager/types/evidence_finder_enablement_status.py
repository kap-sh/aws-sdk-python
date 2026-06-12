"""Generated from Smithy shape ``com.amazonaws.auditmanager#EvidenceFinderEnablementStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

EvidenceFinderEnablementStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ENABLE_IN_PROGRESS",
    "DISABLE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "ENABLE_IN_PROGRESS",
        "DISABLE_IN_PROGRESS",
    )
)


def serialize_json(value: EvidenceFinderEnablementStatus) -> str:
    return value


def deserialize_json(data: str) -> EvidenceFinderEnablementStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvidenceFinderEnablementStatus value: {data!r}"
        )
    return cast(EvidenceFinderEnablementStatus, data)
