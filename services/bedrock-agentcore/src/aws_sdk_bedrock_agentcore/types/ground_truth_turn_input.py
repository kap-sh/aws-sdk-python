"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GroundTruthTurnInput``."""

from typing import TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError


class _GroundTruthTurnInput_prompt(TypedDict):
    prompt: "str"


GroundTruthTurnInput: TypeAlias = _GroundTruthTurnInput_prompt


# --- restJson1 ser/de ---
def serialize_json(value: GroundTruthTurnInput) -> dict:
    if "prompt" in value:
        return {"prompt": value["prompt"]}
    else:
        raise SerializationError("GroundTruthTurnInput: no variant present")


def deserialize_json(data: dict) -> GroundTruthTurnInput:
    if "prompt" in data:
        return {"prompt": data["prompt"]}
    else:
        raise DeserializationError("GroundTruthTurnInput: no recognized variant key")
