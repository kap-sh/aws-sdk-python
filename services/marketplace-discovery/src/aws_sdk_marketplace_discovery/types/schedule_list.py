"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ScheduleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.schedule_item

ScheduleList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.schedule_item.ScheduleItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleList) -> list:
    import aws_sdk_marketplace_discovery.types.schedule_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.schedule_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ScheduleList:
    import aws_sdk_marketplace_discovery.types.schedule_item

    out: ScheduleList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.schedule_item.deserialize_json(item)
        )
    return out
