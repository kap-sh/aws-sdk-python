"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OverrideType``."""

from typing import Literal, TypeAlias, cast

OverrideType: TypeAlias = Literal[
    "SEMANTIC_OVERRIDE",
    "SUMMARY_OVERRIDE",
    "USER_PREFERENCE_OVERRIDE",
    "SELF_MANAGED",
    "EPISODIC_OVERRIDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: OverrideType) -> str:
    return value


def deserialize_json(data: str) -> OverrideType:
    return cast(OverrideType, data)
