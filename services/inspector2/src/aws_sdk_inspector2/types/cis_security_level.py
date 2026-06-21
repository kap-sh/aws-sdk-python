"""Generated from Smithy shape ``com.amazonaws.inspector2#CisSecurityLevel``."""

from typing import Literal, TypeAlias, cast

CisSecurityLevel: TypeAlias = Literal[
    "LEVEL_1",
    "LEVEL_2",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisSecurityLevel) -> str:
    return value


def deserialize_json(data: str) -> CisSecurityLevel:
    return cast(CisSecurityLevel, data)
