"""Generated from Smithy shape ``com.amazonaws.bedrock#KnowledgeBaseConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.retrieve_and_generate_configuration
    import capo_bedrock.types.retrieve_config


class _KnowledgeBaseConfig_retrieveConfig(TypedDict, closed=True):
    retrieveConfig: "capo_bedrock.types.retrieve_config.RetrieveConfig"


class _KnowledgeBaseConfig_retrieveAndGenerateConfig(TypedDict, closed=True):
    retrieveAndGenerateConfig: "capo_bedrock.types.retrieve_and_generate_configuration.RetrieveAndGenerateConfiguration"


KnowledgeBaseConfig: TypeAlias = (
    _KnowledgeBaseConfig_retrieveConfig | _KnowledgeBaseConfig_retrieveAndGenerateConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseConfig) -> dict:
    if "retrieveConfig" in value:
        import capo_bedrock.types.retrieve_config

        return {
            "retrieveConfig": capo_bedrock.types.retrieve_config.serialize_json(
                value["retrieveConfig"]
            )
        }
    elif "retrieveAndGenerateConfig" in value:
        import capo_bedrock.types.retrieve_and_generate_configuration

        return {
            "retrieveAndGenerateConfig": capo_bedrock.types.retrieve_and_generate_configuration.serialize_json(
                value["retrieveAndGenerateConfig"]
            )
        }
    else:
        raise SerializationError("KnowledgeBaseConfig: no variant present")


def deserialize_json(data: dict) -> KnowledgeBaseConfig:
    if "retrieveConfig" in data:
        import capo_bedrock.types.retrieve_config

        return {
            "retrieveConfig": capo_bedrock.types.retrieve_config.deserialize_json(
                data["retrieveConfig"]
            )
        }
    elif "retrieveAndGenerateConfig" in data:
        import capo_bedrock.types.retrieve_and_generate_configuration

        return {
            "retrieveAndGenerateConfig": capo_bedrock.types.retrieve_and_generate_configuration.deserialize_json(
                data["retrieveAndGenerateConfig"]
            )
        }
    else:
        raise DeserializationError("KnowledgeBaseConfig: no recognized variant key")
