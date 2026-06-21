"""Generated from Smithy shape ``com.amazonaws.quicksight#ValueWhenUnsetOption``."""

from typing import Literal, TypeAlias, cast

ValueWhenUnsetOption: TypeAlias = Literal[
    "RECOMMENDED_VALUE",
    "NULL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValueWhenUnsetOption) -> str:
    return value


def deserialize_json(data: str) -> ValueWhenUnsetOption:
    return cast(ValueWhenUnsetOption, data)
