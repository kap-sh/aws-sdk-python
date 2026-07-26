"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConfigurationBundleVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.configuration_bundle_version

ConfigurationBundleVersionList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.configuration_bundle_version.ConfigurationBundleVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleVersionList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConfigurationBundleVersionList:
    return list(data)
