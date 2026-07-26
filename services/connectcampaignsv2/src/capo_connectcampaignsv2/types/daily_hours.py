"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DailyHours``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.day_of_week
    import capo_connectcampaignsv2.types.time_range_list

DailyHours: TypeAlias = dict[
    "capo_connectcampaignsv2.types.day_of_week.DayOfWeek",
    "capo_connectcampaignsv2.types.time_range_list.TimeRangeList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DailyHours) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_connectcampaignsv2.types.time_range_list

        out[key] = capo_connectcampaignsv2.types.time_range_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> DailyHours:
    out: DailyHours = {}
    for key, value in data.items():
        import capo_connectcampaignsv2.types.time_range_list

        out[key] = capo_connectcampaignsv2.types.time_range_list.deserialize_json(value)
    return out
