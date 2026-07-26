"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileQueueConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.routing_profile_queue_config

RoutingProfileQueueConfigList: TypeAlias = list[
    "capo_connect.types.routing_profile_queue_config.RoutingProfileQueueConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileQueueConfigList) -> list:
    import capo_connect.types.routing_profile_queue_config

    out: list = []
    for item in value:
        out.append(capo_connect.types.routing_profile_queue_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoutingProfileQueueConfigList:
    import capo_connect.types.routing_profile_queue_config

    out: RoutingProfileQueueConfigList = []
    for item in data:
        out.append(
            capo_connect.types.routing_profile_queue_config.deserialize_json(item)
        )
    return out
