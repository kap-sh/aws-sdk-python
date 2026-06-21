"""Generated from Smithy shape ``com.amazonaws.groundstation#AuditResults``."""

from typing import Literal, TypeAlias, cast

AuditResults: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditResults) -> str:
    return value


def deserialize_json(data: str) -> AuditResults:
    return cast(AuditResults, data)
