"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ConfigurationBundleToolEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.configuration_bundle_tool_entry

ConfigurationBundleToolEntryList: TypeAlias = list[
    "capo_bedrock_agentcore.types.configuration_bundle_tool_entry.ConfigurationBundleToolEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleToolEntryList) -> list:
    import capo_bedrock_agentcore.types.configuration_bundle_tool_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.configuration_bundle_tool_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfigurationBundleToolEntryList:
    import capo_bedrock_agentcore.types.configuration_bundle_tool_entry

    out: ConfigurationBundleToolEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.configuration_bundle_tool_entry.deserialize_json(
                item
            )
        )
    return out
