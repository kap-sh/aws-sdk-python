"""Generated from Smithy shape ``com.amazonaws.sustainability#TimeGranularity``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the time period over which emissions data is aggregated.</p>"""
TimeGranularity: TypeAlias = Literal[
    "YEARLY_CALENDAR",
    "YEARLY_FISCAL",
    "QUARTERLY_CALENDAR",
    "QUARTERLY_FISCAL",
    "MONTHLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeGranularity) -> str:
    return value


def deserialize_json(data: str) -> TimeGranularity:
    return cast(TimeGranularity, data)
