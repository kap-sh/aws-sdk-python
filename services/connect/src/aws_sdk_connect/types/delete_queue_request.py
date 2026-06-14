"""Generated from Smithy shape ``com.amazonaws.connect#DeleteQueueRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.queue_id


class DeleteQueueRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    queue_id: "aws_sdk_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueueRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQueueRequest:
    out: DeleteQueueRequest = {}  # type: ignore[typeddict-item]
    return out
