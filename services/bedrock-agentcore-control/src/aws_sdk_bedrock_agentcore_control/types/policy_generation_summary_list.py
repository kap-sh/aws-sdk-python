"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyGenerationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.policy_generation_summary

PolicyGenerationSummaryList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.policy_generation_summary.PolicyGenerationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerationSummaryList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.policy_generation_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.policy_generation_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PolicyGenerationSummaryList:
    import aws_sdk_bedrock_agentcore_control.types.policy_generation_summary

    out: PolicyGenerationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.policy_generation_summary.deserialize_json(
                item
            )
        )
    return out
