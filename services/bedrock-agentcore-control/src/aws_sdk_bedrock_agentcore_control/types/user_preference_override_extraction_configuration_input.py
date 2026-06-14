"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UserPreferenceOverrideExtractionConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.prompt


class UserPreferenceOverrideExtractionConfigurationInput(TypedDict):
    append_to_prompt: "aws_sdk_bedrock_agentcore_control.types.prompt.Prompt"
    """<p>The text to append to the prompt for user preference extraction.</p>"""
    model_id: "str"
    """<p>The model ID to use for user preference extraction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserPreferenceOverrideExtractionConfigurationInput) -> dict:
    out: dict = {}
    out["appendToPrompt"] = value["append_to_prompt"]
    out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> UserPreferenceOverrideExtractionConfigurationInput:
    out: UserPreferenceOverrideExtractionConfigurationInput = {}  # type: ignore[typeddict-item]
    if "appendToPrompt" in data:
        out["append_to_prompt"] = data["appendToPrompt"]
    else:
        raise DeserializationError(
            "UserPreferenceOverrideExtractionConfigurationInput.append_to_prompt required"
        )
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError(
            "UserPreferenceOverrideExtractionConfigurationInput.model_id required"
        )
    return out
