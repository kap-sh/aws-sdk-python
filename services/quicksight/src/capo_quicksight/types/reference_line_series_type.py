"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineSeriesType``."""

from typing import Literal, TypeAlias, cast

ReferenceLineSeriesType: TypeAlias = Literal[
    "BAR",
    "LINE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineSeriesType) -> str:
    return value


def deserialize_json(data: str) -> ReferenceLineSeriesType:
    return cast(ReferenceLineSeriesType, data)
