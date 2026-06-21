"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ChoiceReason``."""

from typing import Literal, TypeAlias, cast

ChoiceReason: TypeAlias = Literal[
    "OUT_OF_SCOPE",
    "BUSINESS_PRIORITIES",
    "ARCHITECTURE_CONSTRAINTS",
    "OTHER",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChoiceReason) -> str:
    return value


def deserialize_json(data: str) -> ChoiceReason:
    return cast(ChoiceReason, data)
