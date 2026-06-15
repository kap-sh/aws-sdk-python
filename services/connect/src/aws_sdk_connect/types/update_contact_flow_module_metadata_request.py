"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactFlowModuleMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_module_description
    import aws_sdk_connect.types.contact_flow_module_id
    import aws_sdk_connect.types.contact_flow_module_name
    import aws_sdk_connect.types.contact_flow_module_state
    import aws_sdk_connect.types.instance_id


class UpdateContactFlowModuleMetadataRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_module_id: (
        "aws_sdk_connect.types.contact_flow_module_id.ContactFlowModuleId"
    )
    """<p>The identifier of the flow module.</p>"""
    name: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_name.ContactFlowModuleName"
    ]
    """<p>The name of the flow module.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_description.ContactFlowModuleDescription"
    ]
    """<p>The description of the flow module.</p>"""
    state: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_state.ContactFlowModuleState"
    ]
    """<p>The state of flow module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactFlowModuleMetadataRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "state" in value:
        import aws_sdk_connect.types.contact_flow_module_state

        out["State"] = aws_sdk_connect.types.contact_flow_module_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> UpdateContactFlowModuleMetadataRequest:
    out: UpdateContactFlowModuleMetadataRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "State" in data:
        import aws_sdk_connect.types.contact_flow_module_state

        out["state"] = aws_sdk_connect.types.contact_flow_module_state.deserialize_json(
            data["State"]
        )
    return out
