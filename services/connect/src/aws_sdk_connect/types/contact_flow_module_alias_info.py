"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleAliasInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.contact_flow_module_alias
    import aws_sdk_connect.types.contact_flow_module_description
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.resource_id
    import aws_sdk_connect.types.resource_version
    import aws_sdk_connect.types.timestamp


class ContactFlowModuleAliasInfo(TypedDict):
    contact_flow_module_id: NotRequired["aws_sdk_connect.types.resource_id.ResourceId"]
    """<p>The identifier of the flow module.</p>"""
    contact_flow_module_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow module.</p>"""
    alias_id: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_alias.ContactFlowModuleAlias"
    ]
    """<p>The identifier of the alias.</p>"""
    version: NotRequired["aws_sdk_connect.types.resource_version.ResourceVersion"]
    """<p>The version of the flow module.</p>"""
    name: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_alias.ContactFlowModuleAlias"
    ]
    """<p>The name of the alias.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_description.ContactFlowModuleDescription"
    ]
    """<p>The description of the alias.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModuleAliasInfo) -> dict:
    out: dict = {}
    if "contact_flow_module_id" in value:
        out["ContactFlowModuleId"] = value["contact_flow_module_id"]
    if "contact_flow_module_arn" in value:
        out["ContactFlowModuleArn"] = value["contact_flow_module_arn"]
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "version" in value:
        out["Version"] = value["version"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> ContactFlowModuleAliasInfo:
    out: ContactFlowModuleAliasInfo = {}  # type: ignore[typeddict-item]
    if "ContactFlowModuleId" in data:
        out["contact_flow_module_id"] = data["ContactFlowModuleId"]
    if "ContactFlowModuleArn" in data:
        out["contact_flow_module_arn"] = data["ContactFlowModuleArn"]
    if "AliasId" in data:
        out["alias_id"] = data["AliasId"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    return out
