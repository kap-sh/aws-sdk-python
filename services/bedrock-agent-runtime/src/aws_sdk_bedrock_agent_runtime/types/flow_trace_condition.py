"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceCondition``."""

from typing import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError


class FlowTraceCondition(TypedDict):
    condition_name: "str"
    """<p>The name of the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceCondition) -> dict:
    out: dict = {}
    out["conditionName"] = value["condition_name"]
    return out


def deserialize_json(data: dict) -> FlowTraceCondition:
    out: FlowTraceCondition = {}  # type: ignore[typeddict-item]
    if "conditionName" in data:
        out["condition_name"] = data["conditionName"]
    else:
        raise DeserializationError("FlowTraceCondition.condition_name required")
    return out
