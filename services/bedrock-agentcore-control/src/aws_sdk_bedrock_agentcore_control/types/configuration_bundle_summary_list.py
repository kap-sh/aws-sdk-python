"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConfigurationBundleSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_summary

ConfigurationBundleSummaryList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_summary.ConfigurationBundleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleSummaryList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.configuration_bundle_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfigurationBundleSummaryList:
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_summary

    out: ConfigurationBundleSummaryList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.configuration_bundle_summary.deserialize_json(
                item
            )
        )
    return out
