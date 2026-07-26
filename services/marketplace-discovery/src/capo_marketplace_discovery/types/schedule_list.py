"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ScheduleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.schedule_item

ScheduleList: TypeAlias = list[
    "capo_marketplace_discovery.types.schedule_item.ScheduleItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleList) -> list:
    import capo_marketplace_discovery.types.schedule_item

    out: list = []
    for item in value:
        out.append(capo_marketplace_discovery.types.schedule_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScheduleList:
    import capo_marketplace_discovery.types.schedule_item

    out: ScheduleList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.schedule_item.deserialize_json(item)
        )
    return out
