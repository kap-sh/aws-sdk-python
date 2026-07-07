"""Generated from Smithy shape ``com.amazonaws.bedrock#RAGConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_precomputed_rag_source_config
    import aws_sdk_bedrock.types.knowledge_base_config


class _RAGConfig_knowledgeBaseConfig(TypedDict, closed=True):
    knowledgeBaseConfig: (
        "aws_sdk_bedrock.types.knowledge_base_config.KnowledgeBaseConfig"
    )


class _RAGConfig_precomputedRagSourceConfig(TypedDict, closed=True):
    precomputedRagSourceConfig: "aws_sdk_bedrock.types.evaluation_precomputed_rag_source_config.EvaluationPrecomputedRagSourceConfig"


RAGConfig: TypeAlias = (
    _RAGConfig_knowledgeBaseConfig | _RAGConfig_precomputedRagSourceConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: RAGConfig) -> dict:
    if "knowledgeBaseConfig" in value:
        import aws_sdk_bedrock.types.knowledge_base_config

        return {
            "knowledgeBaseConfig": aws_sdk_bedrock.types.knowledge_base_config.serialize_json(
                value["knowledgeBaseConfig"]
            )
        }
    elif "precomputedRagSourceConfig" in value:
        import aws_sdk_bedrock.types.evaluation_precomputed_rag_source_config

        return {
            "precomputedRagSourceConfig": aws_sdk_bedrock.types.evaluation_precomputed_rag_source_config.serialize_json(
                value["precomputedRagSourceConfig"]
            )
        }
    else:
        raise SerializationError("RAGConfig: no variant present")


def deserialize_json(data: dict) -> RAGConfig:
    if "knowledgeBaseConfig" in data:
        import aws_sdk_bedrock.types.knowledge_base_config

        return {
            "knowledgeBaseConfig": aws_sdk_bedrock.types.knowledge_base_config.deserialize_json(
                data["knowledgeBaseConfig"]
            )
        }
    elif "precomputedRagSourceConfig" in data:
        import aws_sdk_bedrock.types.evaluation_precomputed_rag_source_config

        return {
            "precomputedRagSourceConfig": aws_sdk_bedrock.types.evaluation_precomputed_rag_source_config.deserialize_json(
                data["precomputedRagSourceConfig"]
            )
        }
    else:
        raise DeserializationError("RAGConfig: no recognized variant key")
