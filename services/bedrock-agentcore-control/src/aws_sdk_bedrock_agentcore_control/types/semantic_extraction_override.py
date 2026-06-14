"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SemanticExtractionOverride``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.prompt


class SemanticExtractionOverride(TypedDict):
    append_to_prompt: "aws_sdk_bedrock_agentcore_control.types.prompt.Prompt"
    """<p>The text to append to the prompt for semantic extraction.</p>"""
    model_id: "str"
    """<p>The model ID to use for semantic extraction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemanticExtractionOverride) -> dict:
    out: dict = {}
    out["appendToPrompt"] = value["append_to_prompt"]
    out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> SemanticExtractionOverride:
    out: SemanticExtractionOverride = {}  # type: ignore[typeddict-item]
    if "appendToPrompt" in data:
        out["append_to_prompt"] = data["appendToPrompt"]
    else:
        raise DeserializationError(
            "SemanticExtractionOverride.append_to_prompt required"
        )
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("SemanticExtractionOverride.model_id required")
    return out
