"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_execution_summary

FlowExecutionSummaries: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.flow_execution_summary.FlowExecutionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionSummaries) -> list:
    import capo_bedrock_agent_runtime.types.flow_execution_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.flow_execution_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FlowExecutionSummaries:
    import capo_bedrock_agent_runtime.types.flow_execution_summary

    out: FlowExecutionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.flow_execution_summary.deserialize_json(
                item
            )
        )
    return out
