"""Generated from Smithy shape ``com.amazonaws.neptunedata#DeleteStatisticsValueMap``."""

from typing import TypedDict

from typing_extensions import NotRequired


class DeleteStatisticsValueMap(TypedDict):
    active: NotRequired["bool"]
    """<p>The current status of the statistics.</p>"""
    statistics_id: NotRequired["str"]
    """<p>The ID of the statistics generation run that is currently occurring.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteStatisticsValueMap) -> dict:
    out: dict = {}
    if "active" in value:
        out["active"] = value["active"]
    if "statistics_id" in value:
        out["statisticsId"] = value["statistics_id"]
    return out


def deserialize_json(data: dict) -> DeleteStatisticsValueMap:
    out: DeleteStatisticsValueMap = {}  # type: ignore[typeddict-item]
    if "active" in data:
        out["active"] = data["active"]
    if "statisticsId" in data:
        out["statistics_id"] = data["statisticsId"]
    return out
