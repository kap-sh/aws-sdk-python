"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ConfigurationBundleToolEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.configuration_bundle_tool_entry

ConfigurationBundleToolEntryList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.configuration_bundle_tool_entry.ConfigurationBundleToolEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleToolEntryList) -> list:
    import aws_sdk_bedrock_agentcore.types.configuration_bundle_tool_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.configuration_bundle_tool_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfigurationBundleToolEntryList:
    import aws_sdk_bedrock_agentcore.types.configuration_bundle_tool_entry

    out: ConfigurationBundleToolEntryList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.configuration_bundle_tool_entry.deserialize_json(
                item
            )
        )
    return out
