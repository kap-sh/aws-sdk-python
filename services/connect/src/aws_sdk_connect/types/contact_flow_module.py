"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.contact_flow_module_content
    import aws_sdk_connect.types.contact_flow_module_description
    import aws_sdk_connect.types.contact_flow_module_id
    import aws_sdk_connect.types.contact_flow_module_name
    import aws_sdk_connect.types.contact_flow_module_state
    import aws_sdk_connect.types.contact_flow_module_status
    import aws_sdk_connect.types.external_invocation_configuration
    import aws_sdk_connect.types.flow_module_content_sha256
    import aws_sdk_connect.types.flow_module_settings
    import aws_sdk_connect.types.resource_version
    import aws_sdk_connect.types.tag_map


class ContactFlowModule(TypedDict):
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN).</p>"""
    id: NotRequired["aws_sdk_connect.types.contact_flow_module_id.ContactFlowModuleId"]
    """<p>The identifier of the flow module.</p>"""
    name: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_name.ContactFlowModuleName"
    ]
    """<p>The name of the flow module.</p>"""
    content: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_content.ContactFlowModuleContent"
    ]
    """<p>The JSON string that represents the content of the flow. For an example, see <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/flow-language-example.html\">Example flow in Connect Customer Flow language</a>. </p>"""
    description: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_description.ContactFlowModuleDescription"
    ]
    """<p>The description of the flow module.</p>"""
    state: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_state.ContactFlowModuleState"
    ]
    """<p>The type of flow module.</p>"""
    status: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_status.ContactFlowModuleStatus"
    ]
    """<p>The status of the flow module.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    flow_module_content_sha256: NotRequired[
        "aws_sdk_connect.types.flow_module_content_sha256.FlowModuleContentSha256"
    ]
    """<p>Hash of the module content for integrity verification.</p>"""
    version: NotRequired["aws_sdk_connect.types.resource_version.ResourceVersion"]
    """<p>The version of the flow module.</p>"""
    version_description: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_description.ContactFlowModuleDescription"
    ]
    """<p>Description of the version.</p>"""
    settings: NotRequired[
        "aws_sdk_connect.types.flow_module_settings.FlowModuleSettings"
    ]
    """<p>The configuration settings for the flow module.</p>"""
    external_invocation_configuration: NotRequired[
        "aws_sdk_connect.types.external_invocation_configuration.ExternalInvocationConfiguration"
    ]
    """<p>The external invocation configuration for the flow module</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModule) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "content" in value:
        out["Content"] = value["content"]
    if "description" in value:
        out["Description"] = value["description"]
    if "state" in value:
        import aws_sdk_connect.types.contact_flow_module_state

        out["State"] = aws_sdk_connect.types.contact_flow_module_state.serialize_json(
            value["state"]
        )
    if "status" in value:
        import aws_sdk_connect.types.contact_flow_module_status

        out["Status"] = aws_sdk_connect.types.contact_flow_module_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    if "flow_module_content_sha256" in value:
        out["FlowModuleContentSha256"] = value["flow_module_content_sha256"]
    if "version" in value:
        out["Version"] = value["version"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "settings" in value:
        out["Settings"] = value["settings"]
    if "external_invocation_configuration" in value:
        import aws_sdk_connect.types.external_invocation_configuration

        out["ExternalInvocationConfiguration"] = (
            aws_sdk_connect.types.external_invocation_configuration.serialize_json(
                value["external_invocation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactFlowModule:
    out: ContactFlowModule = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "State" in data:
        import aws_sdk_connect.types.contact_flow_module_state

        out["state"] = aws_sdk_connect.types.contact_flow_module_state.deserialize_json(
            data["State"]
        )
    if "Status" in data:
        import aws_sdk_connect.types.contact_flow_module_status

        out["status"] = (
            aws_sdk_connect.types.contact_flow_module_status.deserialize_json(
                data["Status"]
            )
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "FlowModuleContentSha256" in data:
        out["flow_module_content_sha256"] = data["FlowModuleContentSha256"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "VersionDescription" in data:
        out["version_description"] = data["VersionDescription"]
    if "Settings" in data:
        out["settings"] = data["Settings"]
    if "ExternalInvocationConfiguration" in data:
        import aws_sdk_connect.types.external_invocation_configuration

        out["external_invocation_configuration"] = (
            aws_sdk_connect.types.external_invocation_configuration.deserialize_json(
                data["ExternalInvocationConfiguration"]
            )
        )
    return out
