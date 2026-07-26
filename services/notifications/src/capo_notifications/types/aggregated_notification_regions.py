"""Generated from Smithy shape ``com.amazonaws.notifications#AggregatedNotificationRegions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.region

AggregatedNotificationRegions: TypeAlias = list[
    "capo_notifications.types.region.Region"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedNotificationRegions) -> list:
    return list(value)


def deserialize_json(data: list) -> AggregatedNotificationRegions:
    return list(data)
