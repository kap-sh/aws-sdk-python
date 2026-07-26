"""Generated from Smithy shape ``com.amazonaws.securityhub#DateRangeComparison``."""

from typing import Literal, TypeAlias, cast

DateRangeComparison: TypeAlias = Literal[
    "WITHIN",
    "OLDER_THAN",
]


# --- restJson1 ser/de ---
def serialize_json(value: DateRangeComparison) -> str:
    return value


def deserialize_json(data: str) -> DateRangeComparison:
    return cast(DateRangeComparison, data)
