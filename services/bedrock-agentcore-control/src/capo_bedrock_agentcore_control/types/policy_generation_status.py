"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyGenerationStatus``."""

from typing import Literal, TypeAlias, cast

PolicyGenerationStatus: TypeAlias = Literal[
    "GENERATING",
    "GENERATED",
    "GENERATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> PolicyGenerationStatus:
    return cast(PolicyGenerationStatus, data)
