"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactFlowNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_description
    import aws_sdk_connect.types.contact_flow_id
    import aws_sdk_connect.types.contact_flow_name
    import aws_sdk_connect.types.instance_id


class UpdateContactFlowNameRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    contact_flow_id: "aws_sdk_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow.</p>"""
    name: NotRequired["aws_sdk_connect.types.contact_flow_name.ContactFlowName"]
    """<p>The name of the flow.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.contact_flow_description.ContactFlowDescription"
    ]
    """<p>The description of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactFlowNameRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateContactFlowNameRequest:
    out: UpdateContactFlowNameRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
