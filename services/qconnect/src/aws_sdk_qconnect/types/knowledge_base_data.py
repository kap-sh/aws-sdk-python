"""Generated from Smithy shape ``com.amazonaws.qconnect#KnowledgeBaseData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.description
    import aws_sdk_qconnect.types.failure_reason
    import aws_sdk_qconnect.types.knowledge_base_status
    import aws_sdk_qconnect.types.knowledge_base_type
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.rendering_configuration
    import aws_sdk_qconnect.types.server_side_encryption_configuration
    import aws_sdk_qconnect.types.source_configuration
    import aws_sdk_qconnect.types.sync_status
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid
    import aws_sdk_qconnect.types.vector_ingestion_configuration


class KnowledgeBaseData(TypedDict):
    knowledge_base_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the knowledge base.</p>"""
    knowledge_base_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    name: "aws_sdk_qconnect.types.name.Name"
    """<p>The name of the knowledge base.</p>"""
    knowledge_base_type: "aws_sdk_qconnect.types.knowledge_base_type.KnowledgeBaseType"
    """<p>The type of knowledge base.</p>"""
    status: "aws_sdk_qconnect.types.knowledge_base_status.KnowledgeBaseStatus"
    """<p>The status of the knowledge base.</p>"""
    last_content_modification_time: NotRequired["datetime.datetime"]
    """<p>An epoch timestamp indicating the most recent content modification inside the knowledge base. If no content exists in a knowledge base, this value is unset.</p>"""
    vector_ingestion_configuration: NotRequired[
        "aws_sdk_qconnect.types.vector_ingestion_configuration.VectorIngestionConfiguration"
    ]
    """<p>Contains details about how to ingest the documents in a data source.</p>"""
    source_configuration: NotRequired[
        "aws_sdk_qconnect.types.source_configuration.SourceConfiguration"
    ]
    """<p>Source configuration information about the knowledge base.</p>"""
    rendering_configuration: NotRequired[
        "aws_sdk_qconnect.types.rendering_configuration.RenderingConfiguration"
    ]
    """<p>Information about how to render the content.</p>"""
    server_side_encryption_configuration: NotRequired[
        "aws_sdk_qconnect.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    """<p>The configuration information for the customer managed key used for encryption. </p> <p>This KMS key must have a policy that allows <code>kms:CreateGrant</code>, <code>kms:DescribeKey</code>, <code>kms:Decrypt</code>, and <code>kms:GenerateDataKey*</code> permissions to the IAM identity using the key to invoke Amazon Q in Connect. </p> <p>For more information about setting up a customer managed key for Amazon Q in Connect, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html\">Enable Amazon Q in Connect for your instance</a>.</p>"""
    description: NotRequired["aws_sdk_qconnect.types.description.Description"]
    """<p>The description.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    ingestion_status: NotRequired["aws_sdk_qconnect.types.sync_status.SyncStatus"]
    """<p>Status of ingestion on data source.</p>"""
    ingestion_failure_reasons: NotRequired[
        "aws_sdk_qconnect.types.failure_reason.FailureReason"
    ]
    """<p>List of failure reasons on ingestion per file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseData) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["name"] = value["name"]
    out["knowledgeBaseType"] = value["knowledge_base_type"]
    out["status"] = value["status"]
    if "last_content_modification_time" in value:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["lastContentModificationTime"] = (
            aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
                value["last_content_modification_time"]
            )
        )
    if "vector_ingestion_configuration" in value:
        import aws_sdk_qconnect.types.vector_ingestion_configuration

        out["vectorIngestionConfiguration"] = (
            aws_sdk_qconnect.types.vector_ingestion_configuration.serialize_json(
                value["vector_ingestion_configuration"]
            )
        )
    if "source_configuration" in value:
        import aws_sdk_qconnect.types.source_configuration

        out["sourceConfiguration"] = (
            aws_sdk_qconnect.types.source_configuration.serialize_json(
                value["source_configuration"]
            )
        )
    if "rendering_configuration" in value:
        import aws_sdk_qconnect.types.rendering_configuration

        out["renderingConfiguration"] = (
            aws_sdk_qconnect.types.rendering_configuration.serialize_json(
                value["rendering_configuration"]
            )
        )
    if "server_side_encryption_configuration" in value:
        import aws_sdk_qconnect.types.server_side_encryption_configuration

        out["serverSideEncryptionConfiguration"] = (
            aws_sdk_qconnect.types.server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    if "ingestion_status" in value:
        out["ingestionStatus"] = value["ingestion_status"]
    if "ingestion_failure_reasons" in value:
        import aws_sdk_qconnect.types.failure_reason

        out["ingestionFailureReasons"] = (
            aws_sdk_qconnect.types.failure_reason.serialize_json(
                value["ingestion_failure_reasons"]
            )
        )
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
        import aws_sdk_qconnect.types._prelude.timestamp

        out["last_content_modification_time"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["lastContentModificationTime"]
            )
        )
    if "vectorIngestionConfiguration" in data:
        import aws_sdk_qconnect.types.vector_ingestion_configuration

        out["vector_ingestion_configuration"] = (
            aws_sdk_qconnect.types.vector_ingestion_configuration.deserialize_json(
                data["vectorIngestionConfiguration"]
            )
        )
    if "sourceConfiguration" in data:
        import aws_sdk_qconnect.types.source_configuration

        out["source_configuration"] = (
            aws_sdk_qconnect.types.source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    if "renderingConfiguration" in data:
        import aws_sdk_qconnect.types.rendering_configuration

        out["rendering_configuration"] = (
            aws_sdk_qconnect.types.rendering_configuration.deserialize_json(
                data["renderingConfiguration"]
            )
        )
    if "serverSideEncryptionConfiguration" in data:
        import aws_sdk_qconnect.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            aws_sdk_qconnect.types.server_side_encryption_configuration.deserialize_json(
                data["serverSideEncryptionConfiguration"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    if "ingestionStatus" in data:
        out["ingestion_status"] = data["ingestionStatus"]
    if "ingestionFailureReasons" in data:
        import aws_sdk_qconnect.types.failure_reason

        out["ingestion_failure_reasons"] = (
            aws_sdk_qconnect.types.failure_reason.deserialize_json(
                data["ingestionFailureReasons"]
            )
        )
    return out
