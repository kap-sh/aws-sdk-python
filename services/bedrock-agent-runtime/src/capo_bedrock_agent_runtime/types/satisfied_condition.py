"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#SatisfiedCondition``."""

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError


class SatisfiedCondition(TypedDict, closed=True):
    condition_name: "str"
    """<p>The name of the condition that was satisfied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SatisfiedCondition) -> dict:
    out: dict = {}
    out["conditionName"] = value["condition_name"]
    return out


def deserialize_json(data: dict) -> SatisfiedCondition:
    out: SatisfiedCondition = {}  # type: ignore[typeddict-item]
    if "conditionName" in data:
        out["condition_name"] = data["conditionName"]
    else:
        raise DeserializationError("SatisfiedCondition.condition_name required")
    return out
