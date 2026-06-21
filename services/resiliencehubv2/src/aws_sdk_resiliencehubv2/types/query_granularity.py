"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#QueryGranularity``."""

from typing import Literal, TypeAlias, cast

QueryGranularity: TypeAlias = Literal[
    "HOURLY",
    "DAILY",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryGranularity) -> str:
    return value


def deserialize_json(data: str) -> QueryGranularity:
    return cast(QueryGranularity, data)
