"""Generated from Smithy shape ``com.amazonaws.qconnect#ExternalBedrockKnowledgeBaseConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.access_role_arn
    import aws_sdk_qconnect.types.bedrock_knowledge_base_arn


class ExternalBedrockKnowledgeBaseConfig(TypedDict, closed=True):
    bedrock_knowledge_base_arn: (
        "aws_sdk_qconnect.types.bedrock_knowledge_base_arn.BedrockKnowledgeBaseArn"
    )
    """<p>The Amazon Resource Name (ARN) of the external Bedrock knowledge base.</p>"""
    access_role_arn: "aws_sdk_qconnect.types.access_role_arn.AccessRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role used to access the external Bedrock knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalBedrockKnowledgeBaseConfig) -> dict:
    out: dict = {}
    out["bedrockKnowledgeBaseArn"] = value["bedrock_knowledge_base_arn"]
    out["accessRoleArn"] = value["access_role_arn"]
    return out


def deserialize_json(data: dict) -> ExternalBedrockKnowledgeBaseConfig:
    out: ExternalBedrockKnowledgeBaseConfig = {}  # type: ignore[typeddict-item]
    if "bedrockKnowledgeBaseArn" in data:
        out["bedrock_knowledge_base_arn"] = data["bedrockKnowledgeBaseArn"]
    else:
        raise DeserializationError(
            "ExternalBedrockKnowledgeBaseConfig.bedrock_knowledge_base_arn required"
        )
    if "accessRoleArn" in data:
        out["access_role_arn"] = data["accessRoleArn"]
    else:
        raise DeserializationError(
            "ExternalBedrockKnowledgeBaseConfig.access_role_arn required"
        )
    return out
