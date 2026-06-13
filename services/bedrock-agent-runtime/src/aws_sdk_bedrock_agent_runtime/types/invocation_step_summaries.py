"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationStepSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.invocation_step_summary

InvocationStepSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.invocation_step_summary.InvocationStepSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvocationStepSummaries) -> list:
    import aws_sdk_bedrock_agent_runtime.types.invocation_step_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.invocation_step_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InvocationStepSummaries:
    import aws_sdk_bedrock_agent_runtime.types.invocation_step_summary

    out: InvocationStepSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.invocation_step_summary.deserialize_json(
                item
            )
        )
    return out
