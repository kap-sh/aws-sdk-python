"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantAssociationOutputData``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.external_bedrock_knowledge_base_config
    import aws_sdk_qconnect.types.knowledge_base_association_data


class _AssistantAssociationOutputData_knowledgeBaseAssociation(TypedDict):
    knowledgeBaseAssociation: "aws_sdk_qconnect.types.knowledge_base_association_data.KnowledgeBaseAssociationData"


class _AssistantAssociationOutputData_externalBedrockKnowledgeBaseConfig(TypedDict):
    externalBedrockKnowledgeBaseConfig: "aws_sdk_qconnect.types.external_bedrock_knowledge_base_config.ExternalBedrockKnowledgeBaseConfig"


AssistantAssociationOutputData: TypeAlias = (
    _AssistantAssociationOutputData_knowledgeBaseAssociation
    | _AssistantAssociationOutputData_externalBedrockKnowledgeBaseConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationOutputData) -> dict:
    if "knowledgeBaseAssociation" in value:
        import aws_sdk_qconnect.types.knowledge_base_association_data

        return {
            "knowledgeBaseAssociation": aws_sdk_qconnect.types.knowledge_base_association_data.serialize_json(
                value["knowledgeBaseAssociation"]
            )
        }
    elif "externalBedrockKnowledgeBaseConfig" in value:
        import aws_sdk_qconnect.types.external_bedrock_knowledge_base_config

        return {
            "externalBedrockKnowledgeBaseConfig": aws_sdk_qconnect.types.external_bedrock_knowledge_base_config.serialize_json(
                value["externalBedrockKnowledgeBaseConfig"]
            )
        }
    else:
        raise SerializationError("AssistantAssociationOutputData: no variant present")


def deserialize_json(data: dict) -> AssistantAssociationOutputData:
    if "knowledgeBaseAssociation" in data:
        import aws_sdk_qconnect.types.knowledge_base_association_data

        return {
            "knowledgeBaseAssociation": aws_sdk_qconnect.types.knowledge_base_association_data.deserialize_json(
                data["knowledgeBaseAssociation"]
            )
        }
    elif "externalBedrockKnowledgeBaseConfig" in data:
        import aws_sdk_qconnect.types.external_bedrock_knowledge_base_config

        return {
            "externalBedrockKnowledgeBaseConfig": aws_sdk_qconnect.types.external_bedrock_knowledge_base_config.deserialize_json(
                data["externalBedrockKnowledgeBaseConfig"]
            )
        }
    else:
        raise DeserializationError(
            "AssistantAssociationOutputData: no recognized variant key"
        )
