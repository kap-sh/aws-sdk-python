"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.invocation_summary

InvocationSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.invocation_summary.InvocationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvocationSummaries) -> list:
    import aws_sdk_bedrock_agent_runtime.types.invocation_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.invocation_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InvocationSummaries:
    import aws_sdk_bedrock_agent_runtime.types.invocation_summary

    out: InvocationSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.invocation_summary.deserialize_json(
                item
            )
        )
    return out
