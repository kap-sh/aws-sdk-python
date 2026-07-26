"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TimeSeriesSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.time_series_summary

TimeSeriesSummaries: TypeAlias = list[
    "capo_iotsitewise.types.time_series_summary.TimeSeriesSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesSummaries) -> list:
    import capo_iotsitewise.types.time_series_summary

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.time_series_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TimeSeriesSummaries:
    import capo_iotsitewise.types.time_series_summary

    out: TimeSeriesSummaries = []
    for item in data:
        out.append(capo_iotsitewise.types.time_series_summary.deserialize_json(item))
    return out
