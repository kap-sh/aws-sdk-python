"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError


class _EvaluationContent_text(TypedDict, closed=True):
    text: "str"


EvaluationContent: TypeAlias = _EvaluationContent_text


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationContent) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("EvaluationContent: no variant present")


def deserialize_json(data: dict) -> EvaluationContent:
    if "text" in data:
        return {"text": data["text"]}
    else:
        raise DeserializationError("EvaluationContent: no recognized variant key")
