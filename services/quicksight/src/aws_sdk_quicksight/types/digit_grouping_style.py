"""Generated from Smithy shape ``com.amazonaws.quicksight#DigitGroupingStyle``."""

from typing import Literal, TypeAlias, cast

DigitGroupingStyle: TypeAlias = Literal[
    "DEFAULT",
    "LAKHS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DigitGroupingStyle) -> str:
    return value


def deserialize_json(data: str) -> DigitGroupingStyle:
    return cast(DigitGroupingStyle, data)
