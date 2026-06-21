"""Generated from Smithy shape ``com.amazonaws.iot#AuditFindingSeverity``."""

from typing import Literal, TypeAlias, cast

AuditFindingSeverity: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditFindingSeverity) -> str:
    return value


def deserialize_json(data: str) -> AuditFindingSeverity:
    return cast(AuditFindingSeverity, data)
