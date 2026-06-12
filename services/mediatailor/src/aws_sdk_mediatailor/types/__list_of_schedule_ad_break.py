"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfScheduleAdBreak``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.schedule_ad_break

__listOfScheduleAdBreak: TypeAlias = list[
    "aws_sdk_mediatailor.types.schedule_ad_break.ScheduleAdBreak"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfScheduleAdBreak) -> list:
    import aws_sdk_mediatailor.types.schedule_ad_break

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.schedule_ad_break.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfScheduleAdBreak:
    import aws_sdk_mediatailor.types.schedule_ad_break

    out: __listOfScheduleAdBreak = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.schedule_ad_break.deserialize_json(item))
    return out
