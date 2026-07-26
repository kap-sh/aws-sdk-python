"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ClaimMatchOperatorType``."""

from typing import Literal, TypeAlias, cast

ClaimMatchOperatorType: TypeAlias = Literal[
    "EQUALS",
    "CONTAINS",
    "CONTAINS_ANY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClaimMatchOperatorType) -> str:
    return value


def deserialize_json(data: str) -> ClaimMatchOperatorType:
    return cast(ClaimMatchOperatorType, data)
