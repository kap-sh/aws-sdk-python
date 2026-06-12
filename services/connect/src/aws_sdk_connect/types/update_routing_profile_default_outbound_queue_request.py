"""Generated from Smithy shape ``com.amazonaws.connect#UpdateRoutingProfileDefaultOutboundQueueRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.queue_id
    import aws_sdk_connect.types.routing_profile_id


class UpdateRoutingProfileDefaultOutboundQueueRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    routing_profile_id: "aws_sdk_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile.</p>"""
    default_outbound_queue_id: "aws_sdk_connect.types.queue_id.QueueId"
    """<p>The identifier for the default outbound queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoutingProfileDefaultOutboundQueueRequest) -> dict:
    out: dict = {}
    out["DefaultOutboundQueueId"] = value["default_outbound_queue_id"]
    return out


def deserialize_json(data: dict) -> UpdateRoutingProfileDefaultOutboundQueueRequest:
    out: UpdateRoutingProfileDefaultOutboundQueueRequest = {}  # type: ignore[typeddict-item]
    if "DefaultOutboundQueueId" in data:
        out["default_outbound_queue_id"] = data["DefaultOutboundQueueId"]
    else:
        raise DeserializationError(
            "UpdateRoutingProfileDefaultOutboundQueueRequest.default_outbound_queue_id required"
        )
    return out
