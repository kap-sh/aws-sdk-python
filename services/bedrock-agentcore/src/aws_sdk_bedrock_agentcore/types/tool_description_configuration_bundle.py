"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionConfigurationBundle``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.configuration_bundle_arn
    import aws_sdk_bedrock_agentcore.types.configuration_bundle_tool_entry_list
    import aws_sdk_bedrock_agentcore.types.configuration_bundle_version_id


class ToolDescriptionConfigurationBundle(TypedDict):
    bundle_arn: "aws_sdk_bedrock_agentcore.types.configuration_bundle_arn.ConfigurationBundleArn"
    """<p>The Amazon Resource Name (ARN) of the configuration bundle.</p>"""
    version_id: "aws_sdk_bedrock_agentcore.types.configuration_bundle_version_id.ConfigurationBundleVersionId"
    """<p>The version identifier of the configuration bundle.</p>"""
    tools: "aws_sdk_bedrock_agentcore.types.configuration_bundle_tool_entry_list.ConfigurationBundleToolEntryList"
    """<p>The list of tool entries mapping tool names to their JSON paths within the bundle.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionConfigurationBundle) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["versionId"] = value["version_id"]
    import aws_sdk_bedrock_agentcore.types.configuration_bundle_tool_entry_list

    out["tools"] = (
        aws_sdk_bedrock_agentcore.types.configuration_bundle_tool_entry_list.serialize_json(
            value["tools"]
        )
    )
    return out


def deserialize_json(data: dict) -> ToolDescriptionConfigurationBundle:
    out: ToolDescriptionConfigurationBundle = {}  # type: ignore[typeddict-item]
    if "bundleArn" in data:
        out["bundle_arn"] = data["bundleArn"]
    else:
        raise DeserializationError(
            "ToolDescriptionConfigurationBundle.bundle_arn required"
        )
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    else:
        raise DeserializationError(
            "ToolDescriptionConfigurationBundle.version_id required"
        )
    if "tools" in data:
        import aws_sdk_bedrock_agentcore.types.configuration_bundle_tool_entry_list

        out["tools"] = (
            aws_sdk_bedrock_agentcore.types.configuration_bundle_tool_entry_list.deserialize_json(
                data["tools"]
            )
        )
    else:
        raise DeserializationError("ToolDescriptionConfigurationBundle.tools required")
    return out
