"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OnlineEvaluationConfigSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_summary

OnlineEvaluationConfigSummaryList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_summary.OnlineEvaluationConfigSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OnlineEvaluationConfigSummaryList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OnlineEvaluationConfigSummaryList:
    import aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_summary

    out: OnlineEvaluationConfigSummaryList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.online_evaluation_config_summary.deserialize_json(
                item
            )
        )
    return out
