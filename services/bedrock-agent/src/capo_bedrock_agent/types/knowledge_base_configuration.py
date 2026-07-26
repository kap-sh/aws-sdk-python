"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.kendra_knowledge_base_configuration
    import capo_bedrock_agent.types.knowledge_base_type
    import capo_bedrock_agent.types.sql_knowledge_base_configuration
    import capo_bedrock_agent.types.vector_knowledge_base_configuration


class KnowledgeBaseConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.knowledge_base_type.KnowledgeBaseType"
    """<p>The type of data that the data source is converted into for the knowledge base.</p>"""
    vector_knowledge_base_configuration: NotRequired[
        "capo_bedrock_agent.types.vector_knowledge_base_configuration.VectorKnowledgeBaseConfiguration"
    ]
    """<p>Contains details about the model that's used to convert the data source into vector embeddings.</p>"""
    kendra_knowledge_base_configuration: NotRequired[
        "capo_bedrock_agent.types.kendra_knowledge_base_configuration.KendraKnowledgeBaseConfiguration"
    ]
    """<p>Settings for an Amazon Kendra knowledge base.</p>"""
    sql_knowledge_base_configuration: NotRequired[
        "capo_bedrock_agent.types.sql_knowledge_base_configuration.SqlKnowledgeBaseConfiguration"
    ]
    """<p>Specifies configurations for a knowledge base connected to an SQL database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.knowledge_base_type

    out["type"] = capo_bedrock_agent.types.knowledge_base_type.serialize_json(
        value["type"]
    )
    if "vector_knowledge_base_configuration" in value:
        import capo_bedrock_agent.types.vector_knowledge_base_configuration

        out["vectorKnowledgeBaseConfiguration"] = (
            capo_bedrock_agent.types.vector_knowledge_base_configuration.serialize_json(
                value["vector_knowledge_base_configuration"]
            )
        )
    if "kendra_knowledge_base_configuration" in value:
        import capo_bedrock_agent.types.kendra_knowledge_base_configuration

        out["kendraKnowledgeBaseConfiguration"] = (
            capo_bedrock_agent.types.kendra_knowledge_base_configuration.serialize_json(
                value["kendra_knowledge_base_configuration"]
            )
        )
    if "sql_knowledge_base_configuration" in value:
        import capo_bedrock_agent.types.sql_knowledge_base_configuration

        out["sqlKnowledgeBaseConfiguration"] = (
            capo_bedrock_agent.types.sql_knowledge_base_configuration.serialize_json(
                value["sql_knowledge_base_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> KnowledgeBaseConfiguration:
    out: KnowledgeBaseConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_bedrock_agent.types.knowledge_base_type

        out["type"] = capo_bedrock_agent.types.knowledge_base_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("KnowledgeBaseConfiguration.type required")
    if "vectorKnowledgeBaseConfiguration" in data:
        import capo_bedrock_agent.types.vector_knowledge_base_configuration

        out["vector_knowledge_base_configuration"] = (
            capo_bedrock_agent.types.vector_knowledge_base_configuration.deserialize_json(
                data["vectorKnowledgeBaseConfiguration"]
            )
        )
    if "kendraKnowledgeBaseConfiguration" in data:
        import capo_bedrock_agent.types.kendra_knowledge_base_configuration

        out["kendra_knowledge_base_configuration"] = (
            capo_bedrock_agent.types.kendra_knowledge_base_configuration.deserialize_json(
                data["kendraKnowledgeBaseConfiguration"]
            )
        )
    if "sqlKnowledgeBaseConfiguration" in data:
        import capo_bedrock_agent.types.sql_knowledge_base_configuration

        out["sql_knowledge_base_configuration"] = (
            capo_bedrock_agent.types.sql_knowledge_base_configuration.deserialize_json(
                data["sqlKnowledgeBaseConfiguration"]
            )
        )
    return out
