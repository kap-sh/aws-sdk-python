"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleAliasSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.contact_flow_module_description
    import aws_sdk_connect.types.contact_flow_module_name
    import aws_sdk_connect.types.resource_id
    import aws_sdk_connect.types.resource_version
    import aws_sdk_connect.types.timestamp


class ContactFlowModuleAliasSummary(TypedDict):
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow module alias.</p>"""
    alias_id: NotRequired["aws_sdk_connect.types.resource_id.ResourceId"]
    """<p>The identifier of the alias.</p>"""
    version: NotRequired["aws_sdk_connect.types.resource_version.ResourceVersion"]
    """<p>The version of the flow module.</p>"""
    alias_name: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_name.ContactFlowModuleName"
    ]
    """<p>The name of the alias.</p>"""
    alias_description: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_description.ContactFlowModuleDescription"
    ]
    """<p>The description of the alias.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModuleAliasSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "version" in value:
        out["Version"] = value["version"]
    if "alias_name" in value:
        out["AliasName"] = value["alias_name"]
    if "alias_description" in value:
        out["AliasDescription"] = value["alias_description"]
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> ContactFlowModuleAliasSummary:
    out: ContactFlowModuleAliasSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AliasId" in data:
        out["alias_id"] = data["AliasId"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "AliasName" in data:
        out["alias_name"] = data["AliasName"]
    if "AliasDescription" in data:
        out["alias_description"] = data["AliasDescription"]
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    return out
