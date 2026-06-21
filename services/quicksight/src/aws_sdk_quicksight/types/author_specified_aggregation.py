"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorSpecifiedAggregation``."""

from typing import Literal, TypeAlias, cast

AuthorSpecifiedAggregation: TypeAlias = Literal[
    "COUNT",
    "DISTINCT_COUNT",
    "MIN",
    "MAX",
    "MEDIAN",
    "SUM",
    "AVERAGE",
    "STDEV",
    "STDEVP",
    "VAR",
    "VARP",
    "PERCENTILE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorSpecifiedAggregation) -> str:
    return value


def deserialize_json(data: str) -> AuthorSpecifiedAggregation:
    return cast(AuthorSpecifiedAggregation, data)
