"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UserPreferenceExtractionOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.prompt


class UserPreferenceExtractionOverride(TypedDict, closed=True):
    append_to_prompt: "aws_sdk_bedrock_agentcore_control.types.prompt.Prompt"
    """<p>The text to append to the prompt for user preference extraction.</p>"""
    model_id: "str"
    """<p>The model ID to use for user preference extraction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserPreferenceExtractionOverride) -> dict:
    out: dict = {}
    out["appendToPrompt"] = value["append_to_prompt"]
    out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> UserPreferenceExtractionOverride:
    out: UserPreferenceExtractionOverride = {}  # type: ignore[typeddict-item]
    if "appendToPrompt" in data:
        out["append_to_prompt"] = data["appendToPrompt"]
    else:
        raise DeserializationError(
            "UserPreferenceExtractionOverride.append_to_prompt required"
        )
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("UserPreferenceExtractionOverride.model_id required")
    return out
