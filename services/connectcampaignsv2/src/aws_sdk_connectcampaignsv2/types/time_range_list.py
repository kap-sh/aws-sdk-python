"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TimeRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.time_range

TimeRangeList: TypeAlias = list["aws_sdk_connectcampaignsv2.types.time_range.TimeRange"]


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeList) -> list:
    import aws_sdk_connectcampaignsv2.types.time_range

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcampaignsv2.types.time_range.serialize_json(item))
    return out


def deserialize_json(data: list) -> TimeRangeList:
    import aws_sdk_connectcampaignsv2.types.time_range

    out: TimeRangeList = []
    for item in data:
        out.append(aws_sdk_connectcampaignsv2.types.time_range.deserialize_json(item))
    return out
