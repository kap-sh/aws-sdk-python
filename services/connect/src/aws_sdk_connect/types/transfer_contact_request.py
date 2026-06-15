"""Generated from Smithy shape ``com.amazonaws.connect#TransferContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_resource_id
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.contact_flow_id
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.queue_id


class TransferContactRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    queue_id: NotRequired["aws_sdk_connect.types.queue_id.QueueId"]
    """<p>The identifier for the queue.</p>"""
    user_id: NotRequired["aws_sdk_connect.types.agent_resource_id.AgentResourceId"]
    """<p>The identifier for the user. This can be the ID or the ARN of the user.</p>"""
    contact_flow_id: "aws_sdk_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransferContactRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    if "queue_id" in value:
        out["QueueId"] = value["queue_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    out["ContactFlowId"] = value["contact_flow_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> TransferContactRequest:
    out: TransferContactRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("TransferContactRequest.instance_id required")
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("TransferContactRequest.contact_id required")
    if "QueueId" in data:
        out["queue_id"] = data["QueueId"]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "ContactFlowId" in data:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        raise DeserializationError("TransferContactRequest.contact_flow_id required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
