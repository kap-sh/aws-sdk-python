"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TimeRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.time_range

TimeRangeList: TypeAlias = list["capo_connectcampaignsv2.types.time_range.TimeRange"]


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeList) -> list:
    import capo_connectcampaignsv2.types.time_range

    out: list = []
    for item in value:
        out.append(capo_connectcampaignsv2.types.time_range.serialize_json(item))
    return out


def deserialize_json(data: list) -> TimeRangeList:
    import capo_connectcampaignsv2.types.time_range

    out: TimeRangeList = []
    for item in data:
        out.append(capo_connectcampaignsv2.types.time_range.deserialize_json(item))
    return out
