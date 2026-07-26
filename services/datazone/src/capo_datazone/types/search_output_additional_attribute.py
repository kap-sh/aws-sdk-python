"""Generated from Smithy shape ``com.amazonaws.datazone#SearchOutputAdditionalAttribute``."""

from typing import Literal, TypeAlias, cast

SearchOutputAdditionalAttribute: TypeAlias = Literal[
    "FORMS",
    "TIME_SERIES_DATA_POINT_FORMS",
    "TEXT_MATCH_RATIONALE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchOutputAdditionalAttribute) -> str:
    return value


def deserialize_json(data: str) -> SearchOutputAdditionalAttribute:
    return cast(SearchOutputAdditionalAttribute, data)
