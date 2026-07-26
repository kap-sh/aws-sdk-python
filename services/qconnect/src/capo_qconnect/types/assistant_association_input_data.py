"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantAssociationInputData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.external_bedrock_knowledge_base_config
    import capo_qconnect.types.uuid


class _AssistantAssociationInputData_knowledgeBaseId(TypedDict, closed=True):
    knowledgeBaseId: "capo_qconnect.types.uuid.Uuid"


class _AssistantAssociationInputData_externalBedrockKnowledgeBaseConfig(
    TypedDict, closed=True
):
    externalBedrockKnowledgeBaseConfig: "capo_qconnect.types.external_bedrock_knowledge_base_config.ExternalBedrockKnowledgeBaseConfig"


AssistantAssociationInputData: TypeAlias = (
    _AssistantAssociationInputData_knowledgeBaseId
    | _AssistantAssociationInputData_externalBedrockKnowledgeBaseConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationInputData) -> dict:
    if "knowledgeBaseId" in value:
        return {"knowledgeBaseId": value["knowledgeBaseId"]}
    elif "externalBedrockKnowledgeBaseConfig" in value:
        import capo_qconnect.types.external_bedrock_knowledge_base_config

        return {
            "externalBedrockKnowledgeBaseConfig": capo_qconnect.types.external_bedrock_knowledge_base_config.serialize_json(
                value["externalBedrockKnowledgeBaseConfig"]
            )
        }
    else:
        raise SerializationError("AssistantAssociationInputData: no variant present")


def deserialize_json(data: dict) -> AssistantAssociationInputData:
    if "knowledgeBaseId" in data:
        return {"knowledgeBaseId": data["knowledgeBaseId"]}
    elif "externalBedrockKnowledgeBaseConfig" in data:
        import capo_qconnect.types.external_bedrock_knowledge_base_config

        return {
            "externalBedrockKnowledgeBaseConfig": capo_qconnect.types.external_bedrock_knowledge_base_config.deserialize_json(
                data["externalBedrockKnowledgeBaseConfig"]
            )
        }
    else:
        raise DeserializationError(
            "AssistantAssociationInputData: no recognized variant key"
        )
