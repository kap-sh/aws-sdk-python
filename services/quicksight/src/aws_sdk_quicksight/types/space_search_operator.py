"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceSearchOperator``."""

from typing import Literal, TypeAlias, cast

SpaceSearchOperator: TypeAlias = Literal[
    "STRING_EQUALS",
    "STRING_LIKE",
    "NUMBER_RANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SpaceSearchOperator) -> str:
    return value


def deserialize_json(data: str) -> SpaceSearchOperator:
    return cast(SpaceSearchOperator, data)
