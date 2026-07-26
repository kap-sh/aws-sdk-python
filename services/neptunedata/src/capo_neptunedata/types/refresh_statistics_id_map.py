"""Generated from Smithy shape ``com.amazonaws.neptunedata#RefreshStatisticsIdMap``."""

from typing_extensions import NotRequired, TypedDict


class RefreshStatisticsIdMap(TypedDict, closed=True):
    statistics_id: NotRequired["str"]
    """<p>The ID of the statistics generation run that is currently occurring.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RefreshStatisticsIdMap) -> dict:
    out: dict = {}
    if "statistics_id" in value:
        out["statisticsId"] = value["statistics_id"]
    return out


def deserialize_json(data: dict) -> RefreshStatisticsIdMap:
    out: RefreshStatisticsIdMap = {}  # type: ignore[typeddict-item]
    if "statisticsId" in data:
        out["statistics_id"] = data["statisticsId"]
    return out
