"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ChoiceStatus``."""

from typing import Literal, TypeAlias, cast

ChoiceStatus: TypeAlias = Literal[
    "SELECTED",
    "NOT_APPLICABLE",
    "UNSELECTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChoiceStatus) -> str:
    return value


def deserialize_json(data: str) -> ChoiceStatus:
    return cast(ChoiceStatus, data)
