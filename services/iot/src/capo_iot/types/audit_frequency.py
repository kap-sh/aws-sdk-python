"""Generated from Smithy shape ``com.amazonaws.iot#AuditFrequency``."""

from typing import Literal, TypeAlias, cast

AuditFrequency: TypeAlias = Literal[
    "DAILY",
    "WEEKLY",
    "BIWEEKLY",
    "MONTHLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditFrequency) -> str:
    return value


def deserialize_json(data: str) -> AuditFrequency:
    return cast(AuditFrequency, data)
