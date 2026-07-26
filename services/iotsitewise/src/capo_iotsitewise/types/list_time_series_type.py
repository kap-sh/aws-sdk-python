"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListTimeSeriesType``."""

from typing import Literal, TypeAlias, cast

ListTimeSeriesType: TypeAlias = Literal[
    "ASSOCIATED",
    "DISASSOCIATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTimeSeriesType) -> str:
    return value


def deserialize_json(data: str) -> ListTimeSeriesType:
    return cast(ListTimeSeriesType, data)
