"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileQueueConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.delay
    import aws_sdk_connect.types.priority
    import aws_sdk_connect.types.routing_profile_queue_reference


class RoutingProfileQueueConfig(TypedDict):
    queue_reference: "aws_sdk_connect.types.routing_profile_queue_reference.RoutingProfileQueueReference"
    """<p>Contains information about a queue resource.</p>"""
    priority: "aws_sdk_connect.types.priority.Priority"
    """<p>The order in which contacts are to be handled for the queue. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html\">Queues: priority and delay</a>.</p>"""
    delay: "aws_sdk_connect.types.delay.Delay"
    """<p>The delay, in seconds, a contact should be in the queue before they are routed to an available agent. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html\">Queues: priority and delay</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileQueueConfig) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.routing_profile_queue_reference

    out["QueueReference"] = (
        aws_sdk_connect.types.routing_profile_queue_reference.serialize_json(
            value["queue_reference"]
        )
    )
    out["Priority"] = value["priority"]
    out["Delay"] = value["delay"]
    return out


def deserialize_json(data: dict) -> RoutingProfileQueueConfig:
    out: RoutingProfileQueueConfig = {}  # type: ignore[typeddict-item]
    if "QueueReference" in data:
        import aws_sdk_connect.types.routing_profile_queue_reference

        out["queue_reference"] = (
            aws_sdk_connect.types.routing_profile_queue_reference.deserialize_json(
                data["QueueReference"]
            )
        )
    else:
        raise DeserializationError("RoutingProfileQueueConfig.queue_reference required")
    if "Priority" in data:
        out["priority"] = data["Priority"]
    else:
        raise DeserializationError("RoutingProfileQueueConfig.priority required")
    if "Delay" in data:
        out["delay"] = data["Delay"]
    else:
        raise DeserializationError("RoutingProfileQueueConfig.delay required")
    return out
