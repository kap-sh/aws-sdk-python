"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileQueueReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.channel
    import aws_sdk_connect.types.queue_id


class RoutingProfileQueueReference(TypedDict, closed=True):
    queue_id: "aws_sdk_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    channel: "aws_sdk_connect.types.channel.Channel"
    """<p>The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileQueueReference) -> dict:
    out: dict = {}
    out["QueueId"] = value["queue_id"]
    import aws_sdk_connect.types.channel

    out["Channel"] = aws_sdk_connect.types.channel.serialize_json(value["channel"])
    return out


def deserialize_json(data: dict) -> RoutingProfileQueueReference:
    out: RoutingProfileQueueReference = {}  # type: ignore[typeddict-item]
    if "QueueId" in data:
        out["queue_id"] = data["QueueId"]
    else:
        raise DeserializationError("RoutingProfileQueueReference.queue_id required")
    if "Channel" in data:
        import aws_sdk_connect.types.channel

        out["channel"] = aws_sdk_connect.types.channel.deserialize_json(data["Channel"])
    else:
        raise DeserializationError("RoutingProfileQueueReference.channel required")
    return out
