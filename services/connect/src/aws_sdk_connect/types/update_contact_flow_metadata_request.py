"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactFlowMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_description
    import aws_sdk_connect.types.contact_flow_id
    import aws_sdk_connect.types.contact_flow_name
    import aws_sdk_connect.types.contact_flow_state
    import aws_sdk_connect.types.instance_id


class UpdateContactFlowMetadataRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_id: "aws_sdk_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow.</p>"""
    name: NotRequired["aws_sdk_connect.types.contact_flow_name.ContactFlowName"]
    """<p>The name of the flow.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.contact_flow_description.ContactFlowDescription"
    ]
    """<p>The description of the flow.</p>"""
    contact_flow_state: NotRequired[
        "aws_sdk_connect.types.contact_flow_state.ContactFlowState"
    ]
    """<p>The state of flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactFlowMetadataRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "contact_flow_state" in value:
        import aws_sdk_connect.types.contact_flow_state

        out["ContactFlowState"] = (
            aws_sdk_connect.types.contact_flow_state.serialize_json(
                value["contact_flow_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateContactFlowMetadataRequest:
    out: UpdateContactFlowMetadataRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ContactFlowState" in data:
        import aws_sdk_connect.types.contact_flow_state

        out["contact_flow_state"] = (
            aws_sdk_connect.types.contact_flow_state.deserialize_json(
                data["ContactFlowState"]
            )
        )
    return out
