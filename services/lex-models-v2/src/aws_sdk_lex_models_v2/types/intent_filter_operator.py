"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentFilterOperator``."""

from typing import Literal, TypeAlias, cast

IntentFilterOperator: TypeAlias = Literal[
    "CO",
    "EQ",
]


# --- restJson1 ser/de ---
def serialize_json(value: IntentFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> IntentFilterOperator:
    return cast(IntentFilterOperator, data)
