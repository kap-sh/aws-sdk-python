"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConfigurationBundleVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_summary

ConfigurationBundleVersionSummaryList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_summary.ConfigurationBundleVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleVersionSummaryList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfigurationBundleVersionSummaryList:
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_summary

    out: ConfigurationBundleVersionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.configuration_bundle_version_summary.deserialize_json(
                item
            )
        )
    return out
