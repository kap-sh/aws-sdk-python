"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyEngineSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.policy_engine_summary

PolicyEngineSummaryList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.policy_engine_summary.PolicyEngineSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyEngineSummaryList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.policy_engine_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.policy_engine_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PolicyEngineSummaryList:
    import aws_sdk_bedrock_agentcore_control.types.policy_engine_summary

    out: PolicyEngineSummaryList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.policy_engine_summary.deserialize_json(
                item
            )
        )
    return out
