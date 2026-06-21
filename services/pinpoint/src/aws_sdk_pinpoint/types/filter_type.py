"""Generated from Smithy shape ``com.amazonaws.pinpoint#FilterType``."""

from typing import Literal, TypeAlias, cast

FilterType: TypeAlias = Literal[
    "SYSTEM",
    "ENDPOINT",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterType) -> str:
    return value


def deserialize_json(data: str) -> FilterType:
    return cast(FilterType, data)
