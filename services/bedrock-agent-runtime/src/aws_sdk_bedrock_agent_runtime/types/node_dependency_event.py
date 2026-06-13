"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeDependencyEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.node_name
    import aws_sdk_bedrock_agent_runtime.types.node_trace_elements


class NodeDependencyEvent(TypedDict):
    node_name: "aws_sdk_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node that generated the dependency trace.</p>"""
    timestamp: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The date and time that the dependency trace was generated.</p>"""
    trace_elements: (
        "aws_sdk_bedrock_agent_runtime.types.node_trace_elements.NodeTraceElements"
    )
    """<p>The trace elements containing detailed information about the node execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeDependencyEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = (
        aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["timestamp"]
        )
    )
    import aws_sdk_bedrock_agent_runtime.types.node_trace_elements

    out["traceElements"] = (
        aws_sdk_bedrock_agent_runtime.types.node_trace_elements.serialize_json(
            value["trace_elements"]
        )
    )
    return out


def deserialize_json(data: dict) -> NodeDependencyEvent:
    out: NodeDependencyEvent = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("NodeDependencyEvent.node_name required")
    if "timestamp" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["timestamp"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("NodeDependencyEvent.timestamp required")
    if "traceElements" in data:
        import aws_sdk_bedrock_agent_runtime.types.node_trace_elements

        out["trace_elements"] = (
            aws_sdk_bedrock_agent_runtime.types.node_trace_elements.deserialize_json(
                data["traceElements"]
            )
        )
    else:
        raise DeserializationError("NodeDependencyEvent.trace_elements required")
    return out
