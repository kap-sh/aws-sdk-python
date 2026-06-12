"""Generated from Smithy shape ``com.amazonaws.connect#UpdateQueueStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.queue_id
    import aws_sdk_connect.types.queue_status


class UpdateQueueStatusRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    queue_id: "aws_sdk_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    status: "aws_sdk_connect.types.queue_status.QueueStatus"
    """<p>The status of the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueStatusRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.queue_status

    out["Status"] = aws_sdk_connect.types.queue_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> UpdateQueueStatusRequest:
    out: UpdateQueueStatusRequest = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_connect.types.queue_status

        out["status"] = aws_sdk_connect.types.queue_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("UpdateQueueStatusRequest.status required")
    return out
