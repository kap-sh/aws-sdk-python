"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GroundTruthTurnInput``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError


class _GroundTruthTurnInput_prompt(TypedDict, closed=True):
    prompt: "str"


GroundTruthTurnInput: TypeAlias = _GroundTruthTurnInput_prompt


# --- restJson1 ser/de ---
def serialize_json(value: GroundTruthTurnInput) -> dict:
    if "prompt" in value:
        return {"prompt": value["prompt"]}
    else:
        raise SerializationError("GroundTruthTurnInput: no variant present")


def deserialize_json(data: dict) -> GroundTruthTurnInput:
    if data.get("prompt") is not None:
        return {"prompt": data["prompt"]}
    else:
        raise DeserializationError("GroundTruthTurnInput: no recognized variant key")
