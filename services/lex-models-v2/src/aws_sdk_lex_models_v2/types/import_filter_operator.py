"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportFilterOperator``."""

from typing import Literal, TypeAlias, cast

ImportFilterOperator: TypeAlias = Literal[
    "CO",
    "EQ",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> ImportFilterOperator:
    return cast(ImportFilterOperator, data)
