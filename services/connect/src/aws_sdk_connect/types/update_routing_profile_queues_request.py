"""Generated from Smithy shape ``com.amazonaws.connect#UpdateRoutingProfileQueuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.routing_profile_id
    import aws_sdk_connect.types.routing_profile_queue_config_list


class UpdateRoutingProfileQueuesRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    routing_profile_id: "aws_sdk_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile.</p>"""
    queue_configs: "aws_sdk_connect.types.routing_profile_queue_config_list.RoutingProfileQueueConfigList"
    """<p>The queues to be updated for this routing profile. Queues must first be associated to the routing profile. You can do this using AssociateRoutingProfileQueues.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoutingProfileQueuesRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.routing_profile_queue_config_list

    out["QueueConfigs"] = (
        aws_sdk_connect.types.routing_profile_queue_config_list.serialize_json(
            value["queue_configs"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateRoutingProfileQueuesRequest:
    out: UpdateRoutingProfileQueuesRequest = {}  # type: ignore[typeddict-item]
    if "QueueConfigs" in data:
        import aws_sdk_connect.types.routing_profile_queue_config_list

        out["queue_configs"] = (
            aws_sdk_connect.types.routing_profile_queue_config_list.deserialize_json(
                data["QueueConfigs"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRoutingProfileQueuesRequest.queue_configs required"
        )
    return out
