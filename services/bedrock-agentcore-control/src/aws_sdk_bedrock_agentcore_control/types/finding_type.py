"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FindingType``."""

from typing import Literal, TypeAlias, cast

FindingType: TypeAlias = Literal[
    "VALID",
    "INVALID",
    "NOT_TRANSLATABLE",
    "ALLOW_ALL",
    "ALLOW_NONE",
    "DENY_ALL",
    "DENY_NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingType) -> str:
    return value


def deserialize_json(data: str) -> FindingType:
    return cast(FindingType, data)
