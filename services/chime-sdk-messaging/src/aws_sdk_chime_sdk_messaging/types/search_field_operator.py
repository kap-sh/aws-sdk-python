"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SearchFieldOperator``."""

from typing import Literal, TypeAlias, cast

SearchFieldOperator: TypeAlias = Literal[
    "EQUALS",
    "INCLUDES",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchFieldOperator) -> str:
    return value


def deserialize_json(data: str) -> SearchFieldOperator:
    return cast(SearchFieldOperator, data)
