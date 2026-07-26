"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SystemPromptConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.system_prompt_configuration_bundle
    import capo_bedrock_agentcore.types.system_prompt_text


class _SystemPromptConfig_text(TypedDict, closed=True):
    text: "capo_bedrock_agentcore.types.system_prompt_text.SystemPromptText"


class _SystemPromptConfig_configurationBundle(TypedDict, closed=True):
    configurationBundle: "capo_bedrock_agentcore.types.system_prompt_configuration_bundle.SystemPromptConfigurationBundle"


SystemPromptConfig: TypeAlias = (
    _SystemPromptConfig_text | _SystemPromptConfig_configurationBundle
)


# --- restJson1 ser/de ---
def serialize_json(value: SystemPromptConfig) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "configurationBundle" in value:
        import capo_bedrock_agentcore.types.system_prompt_configuration_bundle

        return {
            "configurationBundle": capo_bedrock_agentcore.types.system_prompt_configuration_bundle.serialize_json(
                value["configurationBundle"]
            )
        }
    else:
        raise SerializationError("SystemPromptConfig: no variant present")


def deserialize_json(data: dict) -> SystemPromptConfig:
    if "text" in data:
        return {"text": data["text"]}
    elif "configurationBundle" in data:
        import capo_bedrock_agentcore.types.system_prompt_configuration_bundle

        return {
            "configurationBundle": capo_bedrock_agentcore.types.system_prompt_configuration_bundle.deserialize_json(
                data["configurationBundle"]
            )
        }
    else:
        raise DeserializationError("SystemPromptConfig: no recognized variant key")
