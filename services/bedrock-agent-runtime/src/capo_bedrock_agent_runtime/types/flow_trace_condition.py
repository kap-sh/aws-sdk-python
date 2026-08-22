"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceCondition``."""

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError


class FlowTraceCondition(TypedDict, closed=True):
    condition_name: "str"
    """<p>The name of the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceCondition) -> dict:
    out: dict = {}
    out["conditionName"] = value["condition_name"]
    return out


def deserialize_json(data: dict) -> FlowTraceCondition:
    out: FlowTraceCondition = {}  # type: ignore[typeddict-item]
    if data.get("conditionName") is not None:
        out["condition_name"] = data["conditionName"]
    else:
        raise DeserializationError("FlowTraceCondition.condition_name required")
    return out
