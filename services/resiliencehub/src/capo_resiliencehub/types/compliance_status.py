"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ComplianceStatus``."""

from typing import Literal, TypeAlias, cast

ComplianceStatus: TypeAlias = Literal[
    "PolicyBreached",
    "PolicyMet",
    "NotApplicable",
    "MissingPolicy",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComplianceStatus) -> str:
    return value


def deserialize_json(data: str) -> ComplianceStatus:
    return cast(ComplianceStatus, data)
