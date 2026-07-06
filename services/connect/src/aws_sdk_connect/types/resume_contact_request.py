"""Generated from Smithy shape ``com.amazonaws.connect#ResumeContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_id
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.instance_id


class ResumeContactRequest(TypedDict, closed=True):
    contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the <code>instanceId</code> in the ARN of the instance.</p>"""
    contact_flow_id: NotRequired["aws_sdk_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResumeContactRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    out["InstanceId"] = value["instance_id"]
    if "contact_flow_id" in value:
        out["ContactFlowId"] = value["contact_flow_id"]
    return out


def deserialize_json(data: dict) -> ResumeContactRequest:
    out: ResumeContactRequest = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("ResumeContactRequest.contact_id required")
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("ResumeContactRequest.instance_id required")
    if "ContactFlowId" in data:
        out["contact_flow_id"] = data["ContactFlowId"]
    return out
