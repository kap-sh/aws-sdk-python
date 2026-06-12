"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileQueueConfigSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.channel
    import aws_sdk_connect.types.delay
    import aws_sdk_connect.types.priority
    import aws_sdk_connect.types.queue_id
    import aws_sdk_connect.types.queue_name


class RoutingProfileQueueConfigSummary(TypedDict):
    queue_id: "aws_sdk_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    queue_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the queue.</p>"""
    queue_name: "aws_sdk_connect.types.queue_name.QueueName"
    """<p>The name of the queue.</p>"""
    priority: "aws_sdk_connect.types.priority.Priority"
    """<p>The order in which contacts are to be handled for the queue. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html\">Queues: priority and delay</a>.</p>"""
    delay: "aws_sdk_connect.types.delay.Delay"
    """<p>The delay, in seconds, that a contact should be in the queue before they are routed to an available agent. For more information, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html\">Queues: priority and delay</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    channel: "aws_sdk_connect.types.channel.Channel"
    """<p>The channels this queue supports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileQueueConfigSummary) -> dict:
    out: dict = {}
    out["QueueId"] = value["queue_id"]
    out["QueueArn"] = value["queue_arn"]
    out["QueueName"] = value["queue_name"]
    out["Priority"] = value["priority"]
    out["Delay"] = value.get("delay", 0)
    import aws_sdk_connect.types.channel

    out["Channel"] = aws_sdk_connect.types.channel.serialize_json(value["channel"])
    return out


def deserialize_json(data: dict) -> RoutingProfileQueueConfigSummary:
    out: RoutingProfileQueueConfigSummary = {}  # type: ignore[typeddict-item]
    if "QueueId" in data:
        out["queue_id"] = data["QueueId"]
    else:
        raise DeserializationError("RoutingProfileQueueConfigSummary.queue_id required")
    if "QueueArn" in data:
        out["queue_arn"] = data["QueueArn"]
    else:
        raise DeserializationError(
            "RoutingProfileQueueConfigSummary.queue_arn required"
        )
    if "QueueName" in data:
        out["queue_name"] = data["QueueName"]
    else:
        raise DeserializationError(
            "RoutingProfileQueueConfigSummary.queue_name required"
        )
    if "Priority" in data:
        out["priority"] = data["Priority"]
    else:
        raise DeserializationError("RoutingProfileQueueConfigSummary.priority required")
    if "Delay" in data:
        out["delay"] = data["Delay"]
    else:
        out["delay"] = 0
    if "Channel" in data:
        import aws_sdk_connect.types.channel

        out["channel"] = aws_sdk_connect.types.channel.deserialize_json(data["Channel"])
    else:
        raise DeserializationError("RoutingProfileQueueConfigSummary.channel required")
    return out
