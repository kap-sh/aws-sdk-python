"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.invocation_summary

InvocationSummaries: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.invocation_summary.InvocationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvocationSummaries) -> list:
    import capo_bedrock_agent_runtime.types.invocation_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.invocation_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InvocationSummaries:
    import capo_bedrock_agent_runtime.types.invocation_summary

    out: InvocationSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.invocation_summary.deserialize_json(item)
        )
    return out
