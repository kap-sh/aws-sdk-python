"""Generated from Smithy shape ``com.amazonaws.qconnect#KnowledgeBaseSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.arn
    import capo_qconnect.types.description
    import capo_qconnect.types.knowledge_base_status
    import capo_qconnect.types.knowledge_base_type
    import capo_qconnect.types.name
    import capo_qconnect.types.rendering_configuration
    import capo_qconnect.types.server_side_encryption_configuration
    import capo_qconnect.types.source_configuration
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid
    import capo_qconnect.types.vector_ingestion_configuration


class KnowledgeBaseSummary(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the knowledge base.</p>"""
    knowledge_base_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    name: "capo_qconnect.types.name.Name"
    """<p>The name of the knowledge base.</p>"""
    knowledge_base_type: "capo_qconnect.types.knowledge_base_type.KnowledgeBaseType"
    """<p>The type of knowledge base.</p>"""
    status: "capo_qconnect.types.knowledge_base_status.KnowledgeBaseStatus"
    """<p>The status of the knowledge base summary.</p>"""
    source_configuration: NotRequired[
        "capo_qconnect.types.source_configuration.SourceConfiguration"
    ]
    """<p>Configuration information about the external data source.</p>"""
    vector_ingestion_configuration: NotRequired[
        "capo_qconnect.types.vector_ingestion_configuration.VectorIngestionConfiguration"
    ]
    """<p>Contains details about how to ingest the documents in a data source.</p>"""
    rendering_configuration: NotRequired[
        "capo_qconnect.types.rendering_configuration.RenderingConfiguration"
    ]
    """<p>Information about how to render the content.</p>"""
    server_side_encryption_configuration: NotRequired[
        "capo_qconnect.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    r"""<p>The configuration information for the customer managed key used for encryption. </p> <p>This KMS key must have a policy that allows <code>kms:CreateGrant</code>, <code>kms:DescribeKey</code>, <code>kms:Decrypt</code>, and <code>kms:GenerateDataKey*</code> permissions to the IAM identity using the key to invoke Amazon Q in Connect. </p> <p>For more information about setting up a customer managed key for Amazon Q in Connect, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html\">Enable Amazon Q in Connect for your instance</a>.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description of the knowledge base.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseSummary) -> dict:
    out: dict = {}
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["name"] = value["name"]
    out["knowledgeBaseType"] = value["knowledge_base_type"]
    out["status"] = value["status"]
    if "source_configuration" in value:
        import capo_qconnect.types.source_configuration

        out["sourceConfiguration"] = (
            capo_qconnect.types.source_configuration.serialize_json(
                value["source_configuration"]
            )
        )
    if "vector_ingestion_configuration" in value:
        import capo_qconnect.types.vector_ingestion_configuration

        out["vectorIngestionConfiguration"] = (
            capo_qconnect.types.vector_ingestion_configuration.serialize_json(
                value["vector_ingestion_configuration"]
            )
        )
    if "rendering_configuration" in value:
        import capo_qconnect.types.rendering_configuration

        out["renderingConfiguration"] = (
            capo_qconnect.types.rendering_configuration.serialize_json(
                value["rendering_configuration"]
            )
        )
    if "server_side_encryption_configuration" in value:
        import capo_qconnect.types.server_side_encryption_configuration

        out["serverSideEncryptionConfiguration"] = (
            capo_qconnect.types.server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> KnowledgeBaseSummary:
    out: KnowledgeBaseSummary = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("KnowledgeBaseSummary.knowledge_base_id required")
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("KnowledgeBaseSummary.knowledge_base_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("KnowledgeBaseSummary.name required")
    if "knowledgeBaseType" in data:
        out["knowledge_base_type"] = data["knowledgeBaseType"]
    else:
        raise DeserializationError("KnowledgeBaseSummary.knowledge_base_type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("KnowledgeBaseSummary.status required")
    if "sourceConfiguration" in data:
        import capo_qconnect.types.source_configuration

        out["source_configuration"] = (
            capo_qconnect.types.source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    if "vectorIngestionConfiguration" in data:
        import capo_qconnect.types.vector_ingestion_configuration

        out["vector_ingestion_configuration"] = (
            capo_qconnect.types.vector_ingestion_configuration.deserialize_json(
                data["vectorIngestionConfiguration"]
            )
        )
    if "renderingConfiguration" in data:
        import capo_qconnect.types.rendering_configuration

        out["rendering_configuration"] = (
            capo_qconnect.types.rendering_configuration.deserialize_json(
                data["renderingConfiguration"]
            )
        )
    if "serverSideEncryptionConfiguration" in data:
        import capo_qconnect.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_qconnect.types.server_side_encryption_configuration.deserialize_json(
                data["serverSideEncryptionConfiguration"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    return out
