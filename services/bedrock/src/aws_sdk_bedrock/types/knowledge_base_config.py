"""Generated from Smithy shape ``com.amazonaws.bedrock#KnowledgeBaseConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.retrieve_and_generate_configuration
    import aws_sdk_bedrock.types.retrieve_config


class _KnowledgeBaseConfig_retrieveConfig(TypedDict):
    retrieveConfig: "aws_sdk_bedrock.types.retrieve_config.RetrieveConfig"


class _KnowledgeBaseConfig_retrieveAndGenerateConfig(TypedDict):
    retrieveAndGenerateConfig: "aws_sdk_bedrock.types.retrieve_and_generate_configuration.RetrieveAndGenerateConfiguration"


KnowledgeBaseConfig: TypeAlias = (
    _KnowledgeBaseConfig_retrieveConfig | _KnowledgeBaseConfig_retrieveAndGenerateConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseConfig) -> dict:
    if "retrieveConfig" in value:
        import aws_sdk_bedrock.types.retrieve_config

        return {
            "retrieveConfig": aws_sdk_bedrock.types.retrieve_config.serialize_json(
                value["retrieveConfig"]
            )
        }
    elif "retrieveAndGenerateConfig" in value:
        import aws_sdk_bedrock.types.retrieve_and_generate_configuration

        return {
            "retrieveAndGenerateConfig": aws_sdk_bedrock.types.retrieve_and_generate_configuration.serialize_json(
                value["retrieveAndGenerateConfig"]
            )
        }
    else:
        raise SerializationError("KnowledgeBaseConfig: no variant present")


def deserialize_json(data: dict) -> KnowledgeBaseConfig:
    if "retrieveConfig" in data:
        import aws_sdk_bedrock.types.retrieve_config

        return {
            "retrieveConfig": aws_sdk_bedrock.types.retrieve_config.deserialize_json(
                data["retrieveConfig"]
            )
        }
    elif "retrieveAndGenerateConfig" in data:
        import aws_sdk_bedrock.types.retrieve_and_generate_configuration

        return {
            "retrieveAndGenerateConfig": aws_sdk_bedrock.types.retrieve_and_generate_configuration.deserialize_json(
                data["retrieveAndGenerateConfig"]
            )
        }
    else:
        raise DeserializationError("KnowledgeBaseConfig: no recognized variant key")
