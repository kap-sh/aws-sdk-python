"""Generated from Smithy shape ``com.amazonaws.inspector2#CisRuleStatus``."""

from typing import Literal, TypeAlias, cast

CisRuleStatus: TypeAlias = Literal[
    "FAILED",
    "PASSED",
    "NOT_EVALUATED",
    "INFORMATIONAL",
    "UNKNOWN",
    "NOT_APPLICABLE",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisRuleStatus) -> str:
    return value


def deserialize_json(data: str) -> CisRuleStatus:
    return cast(CisRuleStatus, data)
