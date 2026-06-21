"""Generated from Smithy shape ``com.amazonaws.inspector2#CisSecurityLevelComparison``."""

from typing import Literal, TypeAlias, cast

CisSecurityLevelComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: CisSecurityLevelComparison) -> str:
    return value


def deserialize_json(data: str) -> CisSecurityLevelComparison:
    return cast(CisSecurityLevelComparison, data)
