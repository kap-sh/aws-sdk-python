"""Generated from Smithy shape ``com.amazonaws.wisdom#KnowledgeBaseData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_wisdom.types.arn
    import aws_sdk_wisdom.types.description
    import aws_sdk_wisdom.types.knowledge_base_status
    import aws_sdk_wisdom.types.knowledge_base_type
    import aws_sdk_wisdom.types.name
    import aws_sdk_wisdom.types.rendering_configuration
    import aws_sdk_wisdom.types.server_side_encryption_configuration
    import aws_sdk_wisdom.types.source_configuration
    import aws_sdk_wisdom.types.tags
    import aws_sdk_wisdom.types.uuid


class KnowledgeBaseData(TypedDict):
    knowledge_base_id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.</p>"""
    knowledge_base_arn: "aws_sdk_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    name: "aws_sdk_wisdom.types.name.Name"
    """<p>The name of the knowledge base.</p>"""
    knowledge_base_type: "aws_sdk_wisdom.types.knowledge_base_type.KnowledgeBaseType"
    """<p>The type of knowledge base.</p>"""
    status: "aws_sdk_wisdom.types.knowledge_base_status.KnowledgeBaseStatus"
    """<p>The status of the knowledge base.</p>"""
    last_content_modification_time: NotRequired["datetime.datetime"]
    """<p>An epoch timestamp indicating the most recent content modification inside the knowledge base. If no content exists in a knowledge base, this value is unset.</p>"""
    source_configuration: NotRequired[
        "aws_sdk_wisdom.types.source_configuration.SourceConfiguration"
    ]
    """<p>Source configuration information about the knowledge base.</p>"""
    rendering_configuration: NotRequired[
        "aws_sdk_wisdom.types.rendering_configuration.RenderingConfiguration"
    ]
    """<p>Information about how to render the content.</p>"""
    server_side_encryption_configuration: NotRequired[
        "aws_sdk_wisdom.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    r"""<p>The configuration information for the customer managed key used for encryption. </p> <p>This KMS key must have a policy that allows <code>kms:CreateGrant</code>, <code>kms:DescribeKey</code>, and <code>kms:Decrypt/kms:GenerateDataKey</code> permissions to the IAM identity using the key to invoke Wisdom. </p> <p>For more information about setting up a customer managed key for Wisdom, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html\">Enable Amazon Connect Wisdom for your instance</a>.</p>"""
    description: NotRequired["aws_sdk_wisdom.types.description.Description"]
    """<p>The description.</p>"""
    tags: NotRequired["aws_sdk_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseData) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["name"] = value["name"]
    out["knowledgeBaseType"] = value["knowledge_base_type"]
    out["status"] = value["status"]
    if "last_content_modification_time" in value:
        import aws_sdk_wisdom.types._prelude.timestamp

        out["lastContentModificationTime"] = (
            aws_sdk_wisdom.types._prelude.timestamp.serialize_json(
                value["last_content_modification_time"]
            )
        )
    if "source_configuration" in value:
        import aws_sdk_wisdom.types.source_configuration

        out["sourceConfiguration"] = (
            aws_sdk_wisdom.types.source_configuration.serialize_json(
                value["source_configuration"]
            )
        )
    if "rendering_configuration" in value:
        import aws_sdk_wisdom.types.rendering_configuration

        out["renderingConfiguration"] = (
            aws_sdk_wisdom.types.rendering_configuration.serialize_json(
                value["rendering_configuration"]
            )
        )
    if "server_side_encryption_configuration" in value:
        import aws_sdk_wisdom.types.server_side_encryption_configuration

        out["serverSideEncryptionConfiguration"] = (
            aws_sdk_wisdom.types.server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_wisdom.types.tags

        out["tags"] = aws_sdk_wisdom.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> KnowledgeBaseData:
    out: KnowledgeBaseData = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("KnowledgeBaseData.knowledge_base_id required")
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("KnowledgeBaseData.knowledge_base_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("KnowledgeBaseData.name required")
    if "knowledgeBaseType" in data:
        out["knowledge_base_type"] = data["knowledgeBaseType"]
    else:
        raise DeserializationError("KnowledgeBaseData.knowledge_base_type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("KnowledgeBaseData.status required")
    if "lastContentModificationTime" in data:
        import aws_sdk_wisdom.types._prelude.timestamp

        out["last_content_modification_time"] = (
            aws_sdk_wisdom.types._prelude.timestamp.deserialize_json(
                data["lastContentModificationTime"]
            )
        )
    if "sourceConfiguration" in data:
        import aws_sdk_wisdom.types.source_configuration

        out["source_configuration"] = (
            aws_sdk_wisdom.types.source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    if "renderingConfiguration" in data:
        import aws_sdk_wisdom.types.rendering_configuration

        out["rendering_configuration"] = (
            aws_sdk_wisdom.types.rendering_configuration.deserialize_json(
                data["renderingConfiguration"]
            )
        )
    if "serverSideEncryptionConfiguration" in data:
        import aws_sdk_wisdom.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            aws_sdk_wisdom.types.server_side_encryption_configuration.deserialize_json(
                data["serverSideEncryptionConfiguration"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_wisdom.types.tags

        out["tags"] = aws_sdk_wisdom.types.tags.deserialize_json(data["tags"])
    return out
