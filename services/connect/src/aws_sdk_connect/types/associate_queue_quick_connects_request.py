"""Generated from Smithy shape ``com.amazonaws.connect#AssociateQueueQuickConnectsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.queue_id
    import aws_sdk_connect.types.quick_connects_list


class AssociateQueueQuickConnectsRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    queue_id: "aws_sdk_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    quick_connect_ids: "aws_sdk_connect.types.quick_connects_list.QuickConnectsList"
    """<p>The quick connects to associate with this queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateQueueQuickConnectsRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.quick_connects_list

    out["QuickConnectIds"] = aws_sdk_connect.types.quick_connects_list.serialize_json(
        value["quick_connect_ids"]
    )
    return out


def deserialize_json(data: dict) -> AssociateQueueQuickConnectsRequest:
    out: AssociateQueueQuickConnectsRequest = {}  # type: ignore[typeddict-item]
    if "QuickConnectIds" in data:
        import aws_sdk_connect.types.quick_connects_list

        out["quick_connect_ids"] = (
            aws_sdk_connect.types.quick_connects_list.deserialize_json(
                data["QuickConnectIds"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateQueueQuickConnectsRequest.quick_connect_ids required"
        )
    return out
