"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactFlowModuleAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_module_description
    import aws_sdk_connect.types.contact_flow_module_id
    import aws_sdk_connect.types.contact_flow_module_name
    import aws_sdk_connect.types.instance_id_or_arn
    import aws_sdk_connect.types.resource_id
    import aws_sdk_connect.types.resource_version


class UpdateContactFlowModuleAliasRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_module_id: (
        "aws_sdk_connect.types.contact_flow_module_id.ContactFlowModuleId"
    )
    """<p>The identifier of the flow module.</p>"""
    alias_id: "aws_sdk_connect.types.resource_id.ResourceId"
    """<p>The identifier of the alias.</p>"""
    name: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_name.ContactFlowModuleName"
    ]
    """<p>The name of the alias.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_description.ContactFlowModuleDescription"
    ]
    """<p>The description of the alias.</p>"""
    contact_flow_module_version: NotRequired[
        "aws_sdk_connect.types.resource_version.ResourceVersion"
    ]
    """<p>The version of the flow module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactFlowModuleAliasRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "contact_flow_module_version" in value:
        out["ContactFlowModuleVersion"] = value["contact_flow_module_version"]
    return out


def deserialize_json(data: dict) -> UpdateContactFlowModuleAliasRequest:
    out: UpdateContactFlowModuleAliasRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ContactFlowModuleVersion" in data:
        out["contact_flow_module_version"] = data["ContactFlowModuleVersion"]
    return out
