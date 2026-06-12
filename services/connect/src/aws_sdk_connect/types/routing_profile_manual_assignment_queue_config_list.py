"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileManualAssignmentQueueConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.routing_profile_manual_assignment_queue_config

RoutingProfileManualAssignmentQueueConfigList: TypeAlias = list[
    "aws_sdk_connect.types.routing_profile_manual_assignment_queue_config.RoutingProfileManualAssignmentQueueConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileManualAssignmentQueueConfigList) -> list:
    import aws_sdk_connect.types.routing_profile_manual_assignment_queue_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.routing_profile_manual_assignment_queue_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RoutingProfileManualAssignmentQueueConfigList:
    import aws_sdk_connect.types.routing_profile_manual_assignment_queue_config

    out: RoutingProfileManualAssignmentQueueConfigList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.routing_profile_manual_assignment_queue_config.deserialize_json(
                item
            )
        )
    return out
