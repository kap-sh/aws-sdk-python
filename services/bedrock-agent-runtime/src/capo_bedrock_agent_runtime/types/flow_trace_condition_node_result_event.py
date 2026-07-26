"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceConditionNodeResultEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.flow_trace_conditions
    import capo_bedrock_agent_runtime.types.node_name


class FlowTraceConditionNodeResultEvent(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the condition node.</p>"""
    timestamp: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The date and time that the trace was returned.</p>"""
    satisfied_conditions: (
        "capo_bedrock_agent_runtime.types.flow_trace_conditions.FlowTraceConditions"
    )
    """<p>An array of objects containing information about the conditions that were satisfied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceConditionNodeResultEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
        value["timestamp"]
    )
    import capo_bedrock_agent_runtime.types.flow_trace_conditions

    out["satisfiedConditions"] = (
        capo_bedrock_agent_runtime.types.flow_trace_conditions.serialize_json(
            value["satisfied_conditions"]
        )
    )
    return out


def deserialize_json(data: dict) -> FlowTraceConditionNodeResultEvent:
    out: FlowTraceConditionNodeResultEvent = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError(
            "FlowTraceConditionNodeResultEvent.node_name required"
        )
    if "timestamp" in data:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["timestamp"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError(
            "FlowTraceConditionNodeResultEvent.timestamp required"
        )
    if "satisfiedConditions" in data:
        import capo_bedrock_agent_runtime.types.flow_trace_conditions

        out["satisfied_conditions"] = (
            capo_bedrock_agent_runtime.types.flow_trace_conditions.deserialize_json(
                data["satisfiedConditions"]
            )
        )
    else:
        raise DeserializationError(
            "FlowTraceConditionNodeResultEvent.satisfied_conditions required"
        )
    return out
