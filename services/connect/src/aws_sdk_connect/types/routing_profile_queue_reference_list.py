"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileQueueReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.routing_profile_queue_reference

RoutingProfileQueueReferenceList: TypeAlias = list[
    "aws_sdk_connect.types.routing_profile_queue_reference.RoutingProfileQueueReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileQueueReferenceList) -> list:
    import aws_sdk_connect.types.routing_profile_queue_reference

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.routing_profile_queue_reference.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RoutingProfileQueueReferenceList:
    import aws_sdk_connect.types.routing_profile_queue_reference

    out: RoutingProfileQueueReferenceList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.routing_profile_queue_reference.deserialize_json(item)
        )
    return out
