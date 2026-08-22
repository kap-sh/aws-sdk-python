"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeFailureEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.node_error_code
    import capo_bedrock_agent_runtime.types.node_name


class NodeFailureEvent(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node where the failure occurred.</p>"""
    timestamp: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the node failure occurred.</p>"""
    error_code: "capo_bedrock_agent_runtime.types.node_error_code.NodeErrorCode"
    """<p>The error code that identifies the type of failure that occurred at the node.</p>"""
    error_message: "str"
    """<p>A descriptive message that provides details about the node failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeFailureEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
        value["timestamp"]
    )
    import capo_bedrock_agent_runtime.types.node_error_code

    out["errorCode"] = capo_bedrock_agent_runtime.types.node_error_code.serialize_json(
        value["error_code"]
    )
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> NodeFailureEvent:
    out: NodeFailureEvent = {}  # type: ignore[typeddict-item]
    if data.get("nodeName") is not None:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("NodeFailureEvent.node_name required")
    if data.get("timestamp") is not None:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["timestamp"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("NodeFailureEvent.timestamp required")
    if data.get("errorCode") is not None:
        import capo_bedrock_agent_runtime.types.node_error_code

        out["error_code"] = (
            capo_bedrock_agent_runtime.types.node_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        raise DeserializationError("NodeFailureEvent.error_code required")
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("NodeFailureEvent.error_message required")
    return out
