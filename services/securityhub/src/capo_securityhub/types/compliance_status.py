"""Generated from Smithy shape ``com.amazonaws.securityhub#ComplianceStatus``."""

from typing import Literal, TypeAlias, cast

ComplianceStatus: TypeAlias = Literal[
    "PASSED",
    "WARNING",
    "FAILED",
    "NOT_AVAILABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComplianceStatus) -> str:
    return value


def deserialize_json(data: str) -> ComplianceStatus:
    return cast(ComplianceStatus, data)
