"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeOutputEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.node_name
    import aws_sdk_bedrock_agent_runtime.types.node_output_fields


class NodeOutputEvent(TypedDict):
    node_name: "aws_sdk_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node that produced the outputs.</p>"""
    timestamp: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the outputs were produced by the node.</p>"""
    fields: "aws_sdk_bedrock_agent_runtime.types.node_output_fields.NodeOutputFields"
    """<p>A list of output fields produced by the node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeOutputEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = (
        aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["timestamp"]
        )
    )
    import aws_sdk_bedrock_agent_runtime.types.node_output_fields

    out["fields"] = (
        aws_sdk_bedrock_agent_runtime.types.node_output_fields.serialize_json(
            value["fields"]
        )
    )
    return out


def deserialize_json(data: dict) -> NodeOutputEvent:
    out: NodeOutputEvent = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("NodeOutputEvent.node_name required")
    if "timestamp" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["timestamp"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("NodeOutputEvent.timestamp required")
    if "fields" in data:
        import aws_sdk_bedrock_agent_runtime.types.node_output_fields

        out["fields"] = (
            aws_sdk_bedrock_agent_runtime.types.node_output_fields.deserialize_json(
                data["fields"]
            )
        )
    else:
        raise DeserializationError("NodeOutputEvent.fields required")
    return out
