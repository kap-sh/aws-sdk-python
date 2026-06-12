"""Generated from Smithy shape ``com.amazonaws.iot#AuditFindingSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AuditFindingSeverity: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CRITICAL",
        "HIGH",
        "MEDIUM",
        "LOW",
    )
)


def serialize_json(value: AuditFindingSeverity) -> str:
    return value


def deserialize_json(data: str) -> AuditFindingSeverity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuditFindingSeverity value: {data!r}")
    return cast(AuditFindingSeverity, data)
