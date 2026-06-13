"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ConditionResultEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp
    import aws_sdk_bedrock_agent_runtime.types.node_name
    import aws_sdk_bedrock_agent_runtime.types.satisfied_conditions


class ConditionResultEvent(TypedDict):
    node_name: "aws_sdk_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the condition node that evaluated the conditions.</p>"""
    timestamp: "aws_sdk_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the condition evaluation occurred.</p>"""
    satisfied_conditions: (
        "aws_sdk_bedrock_agent_runtime.types.satisfied_conditions.SatisfiedConditions"
    )
    """<p>A list of conditions that were satisfied during the evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionResultEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import aws_sdk_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = (
        aws_sdk_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["timestamp"]
        )
    )
    import aws_sdk_bedrock_agent_runtime.types.satisfied_conditions

    out["satisfiedConditions"] = (
        aws_sdk_bedrock_agent_runtime.types.satisfied_conditions.serialize_json(
            value["satisfied_conditions"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConditionResultEvent:
    out: ConditionResultEvent = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("ConditionResultEvent.node_name required")
    if "timestamp" in data:
        import aws_sdk_bedrock_agent_runtime.types.date_timestamp

        out["timestamp"] = (
            aws_sdk_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("ConditionResultEvent.timestamp required")
    if "satisfiedConditions" in data:
        import aws_sdk_bedrock_agent_runtime.types.satisfied_conditions

        out["satisfied_conditions"] = (
            aws_sdk_bedrock_agent_runtime.types.satisfied_conditions.deserialize_json(
                data["satisfiedConditions"]
            )
        )
    else:
        raise DeserializationError("ConditionResultEvent.satisfied_conditions required")
    return out
