"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileManualAssignmentQueueConfigSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.channel
    import aws_sdk_connect.types.queue_id
    import aws_sdk_connect.types.queue_name


class RoutingProfileManualAssignmentQueueConfigSummary(TypedDict):
    queue_id: "aws_sdk_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    queue_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the queue.</p>"""
    queue_name: "aws_sdk_connect.types.queue_name.QueueName"
    """<p>The name of the queue.</p>"""
    channel: "aws_sdk_connect.types.channel.Channel"
    """<p>The channels this queue supports. Valid Values: CHAT | TASK | EMAIL </p> <important> <p>VOICE is not supported. The information shown below is incorrect. We're working to correct it. </p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileManualAssignmentQueueConfigSummary) -> dict:
    out: dict = {}
    out["QueueId"] = value["queue_id"]
    out["QueueArn"] = value["queue_arn"]
    out["QueueName"] = value["queue_name"]
    import aws_sdk_connect.types.channel

    out["Channel"] = aws_sdk_connect.types.channel.serialize_json(value["channel"])
    return out


def deserialize_json(data: dict) -> RoutingProfileManualAssignmentQueueConfigSummary:
    out: RoutingProfileManualAssignmentQueueConfigSummary = {}  # type: ignore[typeddict-item]
    if "QueueId" in data:
        out["queue_id"] = data["QueueId"]
    else:
        raise DeserializationError(
            "RoutingProfileManualAssignmentQueueConfigSummary.queue_id required"
        )
    if "QueueArn" in data:
        out["queue_arn"] = data["QueueArn"]
    else:
        raise DeserializationError(
            "RoutingProfileManualAssignmentQueueConfigSummary.queue_arn required"
        )
    if "QueueName" in data:
        out["queue_name"] = data["QueueName"]
    else:
        raise DeserializationError(
            "RoutingProfileManualAssignmentQueueConfigSummary.queue_name required"
        )
    if "Channel" in data:
        import aws_sdk_connect.types.channel

        out["channel"] = aws_sdk_connect.types.channel.deserialize_json(data["Channel"])
    else:
        raise DeserializationError(
            "RoutingProfileManualAssignmentQueueConfigSummary.channel required"
        )
    return out
