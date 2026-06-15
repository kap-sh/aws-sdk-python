"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ConfigurationBundleToolEntry``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.recommendation_tool_name


class ConfigurationBundleToolEntry(TypedDict):
    tool_name: "aws_sdk_bedrock_agentcore.types.recommendation_tool_name.RecommendationToolName"
    """<p>The name of the tool.</p>"""
    tool_description_json_path: "str"
    """<p>The JSON path within the configuration bundle's components that contains the tool description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleToolEntry) -> dict:
    out: dict = {}
    out["toolName"] = value["tool_name"]
    out["toolDescriptionJsonPath"] = value["tool_description_json_path"]
    return out


def deserialize_json(data: dict) -> ConfigurationBundleToolEntry:
    out: ConfigurationBundleToolEntry = {}  # type: ignore[typeddict-item]
    if "toolName" in data:
        out["tool_name"] = data["toolName"]
    else:
        raise DeserializationError("ConfigurationBundleToolEntry.tool_name required")
    if "toolDescriptionJsonPath" in data:
        out["tool_description_json_path"] = data["toolDescriptionJsonPath"]
    else:
        raise DeserializationError(
            "ConfigurationBundleToolEntry.tool_description_json_path required"
        )
    return out
