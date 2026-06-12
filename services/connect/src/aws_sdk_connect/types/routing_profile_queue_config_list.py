"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileQueueConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.routing_profile_queue_config

RoutingProfileQueueConfigList: TypeAlias = list[
    "aws_sdk_connect.types.routing_profile_queue_config.RoutingProfileQueueConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileQueueConfigList) -> list:
    import aws_sdk_connect.types.routing_profile_queue_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.routing_profile_queue_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RoutingProfileQueueConfigList:
    import aws_sdk_connect.types.routing_profile_queue_config

    out: RoutingProfileQueueConfigList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.routing_profile_queue_config.deserialize_json(item)
        )
    return out
