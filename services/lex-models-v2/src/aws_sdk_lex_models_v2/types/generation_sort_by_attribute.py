"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GenerationSortByAttribute``."""

from typing import Literal, TypeAlias, cast

GenerationSortByAttribute: TypeAlias = Literal[
    "creationStartTime",
    "lastUpdatedTime",
]


# --- restJson1 ser/de ---
def serialize_json(value: GenerationSortByAttribute) -> str:
    return value


def deserialize_json(data: str) -> GenerationSortByAttribute:
    return cast(GenerationSortByAttribute, data)
