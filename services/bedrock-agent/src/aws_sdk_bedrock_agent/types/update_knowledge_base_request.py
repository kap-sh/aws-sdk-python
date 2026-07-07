"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.knowledge_base_configuration
    import aws_sdk_bedrock_agent.types.knowledge_base_role_arn
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.storage_configuration


class UpdateKnowledgeBaseRequest(TypedDict, closed=True):
    knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base to update.</p>"""
    name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>Specifies a new name for the knowledge base.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>Specifies a new description for the knowledge base.</p>"""
    role_arn: "aws_sdk_bedrock_agent.types.knowledge_base_role_arn.KnowledgeBaseRoleArn"
    """<p>Specifies a different Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.</p>"""
    knowledge_base_configuration: "aws_sdk_bedrock_agent.types.knowledge_base_configuration.KnowledgeBaseConfiguration"
    """<p>Specifies the configuration for the embeddings model used for the knowledge base. You must use the same configuration as when the knowledge base was created.</p>"""
    storage_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.storage_configuration.StorageConfiguration"
    ]
    """<p>Specifies the configuration for the vector store used for the knowledge base. You must use the same configuration as when the knowledge base was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKnowledgeBaseRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["roleArn"] = value["role_arn"]
    import aws_sdk_bedrock_agent.types.knowledge_base_configuration

    out["knowledgeBaseConfiguration"] = (
        aws_sdk_bedrock_agent.types.knowledge_base_configuration.serialize_json(
            value["knowledge_base_configuration"]
        )
    )
    if "storage_configuration" in value:
        import aws_sdk_bedrock_agent.types.storage_configuration

        out["storageConfiguration"] = (
            aws_sdk_bedrock_agent.types.storage_configuration.serialize_json(
                value["storage_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateKnowledgeBaseRequest:
    out: UpdateKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateKnowledgeBaseRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("UpdateKnowledgeBaseRequest.role_arn required")
    if "knowledgeBaseConfiguration" in data:
        import aws_sdk_bedrock_agent.types.knowledge_base_configuration

        out["knowledge_base_configuration"] = (
            aws_sdk_bedrock_agent.types.knowledge_base_configuration.deserialize_json(
                data["knowledgeBaseConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateKnowledgeBaseRequest.knowledge_base_configuration required"
        )
    if "storageConfiguration" in data:
        import aws_sdk_bedrock_agent.types.storage_configuration

        out["storage_configuration"] = (
            aws_sdk_bedrock_agent.types.storage_configuration.deserialize_json(
                data["storageConfiguration"]
            )
        )
    return out
