"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ConditionResultEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.node_name
    import capo_bedrock_agent_runtime.types.satisfied_conditions


class ConditionResultEvent(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the condition node that evaluated the conditions.</p>"""
    timestamp: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the condition evaluation occurred.</p>"""
    satisfied_conditions: (
        "capo_bedrock_agent_runtime.types.satisfied_conditions.SatisfiedConditions"
    )
    """<p>A list of conditions that were satisfied during the evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionResultEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
        value["timestamp"]
    )
    import capo_bedrock_agent_runtime.types.satisfied_conditions

    out["satisfiedConditions"] = (
        capo_bedrock_agent_runtime.types.satisfied_conditions.serialize_json(
            value["satisfied_conditions"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConditionResultEvent:
    out: ConditionResultEvent = {}  # type: ignore[typeddict-item]
    if data.get("nodeName") is not None:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("ConditionResultEvent.node_name required")
    if data.get("timestamp") is not None:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["timestamp"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("ConditionResultEvent.timestamp required")
    if data.get("satisfiedConditions") is not None:
        import capo_bedrock_agent_runtime.types.satisfied_conditions

        out["satisfied_conditions"] = (
            capo_bedrock_agent_runtime.types.satisfied_conditions.deserialize_json(
                data["satisfiedConditions"]
            )
        )
    else:
        raise DeserializationError("ConditionResultEvent.satisfied_conditions required")
    return out
