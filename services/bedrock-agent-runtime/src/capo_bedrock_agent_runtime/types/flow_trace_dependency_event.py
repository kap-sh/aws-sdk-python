"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceDependencyEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.node_name
    import capo_bedrock_agent_runtime.types.trace_elements


class FlowTraceDependencyEvent(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node that generated the dependency trace.</p>"""
    timestamp: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The date and time that the dependency trace was generated.</p>"""
    trace_elements: "capo_bedrock_agent_runtime.types.trace_elements.TraceElements"
    """<p>The trace elements containing detailed information about the dependency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceDependencyEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
        value["timestamp"]
    )
    import capo_bedrock_agent_runtime.types.trace_elements

    out["traceElements"] = (
        capo_bedrock_agent_runtime.types.trace_elements.serialize_json(
            value["trace_elements"]
        )
    )
    return out


def deserialize_json(data: dict) -> FlowTraceDependencyEvent:
    out: FlowTraceDependencyEvent = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("FlowTraceDependencyEvent.node_name required")
    if "timestamp" in data:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["timestamp"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("FlowTraceDependencyEvent.timestamp required")
    if "traceElements" in data:
        import capo_bedrock_agent_runtime.types.trace_elements

        out["trace_elements"] = (
            capo_bedrock_agent_runtime.types.trace_elements.deserialize_json(
                data["traceElements"]
            )
        )
    else:
        raise DeserializationError("FlowTraceDependencyEvent.trace_elements required")
    return out
