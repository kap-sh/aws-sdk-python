"""Generated from Smithy shape ``com.amazonaws.iotevents#RoutedResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events.types.routed_resource

RoutedResources: TypeAlias = list[
    "capo_iot_events.types.routed_resource.RoutedResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutedResources) -> list:
    import capo_iot_events.types.routed_resource

    out: list = []
    for item in value:
        out.append(capo_iot_events.types.routed_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoutedResources:
    import capo_iot_events.types.routed_resource

    out: RoutedResources = []
    for item in data:
        out.append(capo_iot_events.types.routed_resource.deserialize_json(item))
    return out
