"""Generated from Smithy shape ``com.amazonaws.qconnect#ImportJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.content_metadata
    import aws_sdk_qconnect.types.external_source_configuration
    import aws_sdk_qconnect.types.import_job_status
    import aws_sdk_qconnect.types.import_job_type
    import aws_sdk_qconnect.types.upload_id
    import aws_sdk_qconnect.types.uuid


class ImportJobSummary(TypedDict):
    import_job_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the import job.</p>"""
    knowledge_base_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the knowledge base.</p>"""
    upload_id: "aws_sdk_qconnect.types.upload_id.UploadId"
    """<p>A pointer to the uploaded asset. This value is returned by <a href=\"https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html\">StartContentUpload</a>.</p>"""
    knowledge_base_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    import_job_type: "aws_sdk_qconnect.types.import_job_type.ImportJobType"
    """<p>The type of import job.</p>"""
    status: "aws_sdk_qconnect.types.import_job_status.ImportJobStatus"
    """<p>The status of the import job.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the import job was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp when the import job was last modified.</p>"""
    metadata: NotRequired["aws_sdk_qconnect.types.content_metadata.ContentMetadata"]
    """<p>The metadata fields of the imported Amazon Q in Connect resources.</p>"""
    external_source_configuration: NotRequired[
        "aws_sdk_qconnect.types.external_source_configuration.ExternalSourceConfiguration"
    ]
    """<p>The configuration information of the external source that the resource data are imported from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportJobSummary) -> dict:
    out: dict = {}
    out["importJobId"] = value["import_job_id"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["uploadId"] = value["upload_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["importJobType"] = value["import_job_type"]
    out["status"] = value["status"]
    import aws_sdk_qconnect.types._prelude.timestamp

    out["createdTime"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
        value["created_time"]
    )
    import aws_sdk_qconnect.types._prelude.timestamp

    out["lastModifiedTime"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "metadata" in value:
        import aws_sdk_qconnect.types.content_metadata

        out["metadata"] = aws_sdk_qconnect.types.content_metadata.serialize_json(
            value["metadata"]
        )
    if "external_source_configuration" in value:
        import aws_sdk_qconnect.types.external_source_configuration

        out["externalSourceConfiguration"] = (
            aws_sdk_qconnect.types.external_source_configuration.serialize_json(
                value["external_source_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImportJobSummary:
    out: ImportJobSummary = {}  # type: ignore[typeddict-item]
    if "importJobId" in data:
        out["import_job_id"] = data["importJobId"]
    else:
        raise DeserializationError("ImportJobSummary.import_job_id required")
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("ImportJobSummary.knowledge_base_id required")
    if "uploadId" in data:
        out["upload_id"] = data["uploadId"]
    else:
        raise DeserializationError("ImportJobSummary.upload_id required")
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("ImportJobSummary.knowledge_base_arn required")
    if "importJobType" in data:
        out["import_job_type"] = data["importJobType"]
    else:
        raise DeserializationError("ImportJobSummary.import_job_type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ImportJobSummary.status required")
    if "createdTime" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["created_time"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        raise DeserializationError("ImportJobSummary.created_time required")
    if "lastModifiedTime" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("ImportJobSummary.last_modified_time required")
    if "metadata" in data:
        import aws_sdk_qconnect.types.content_metadata

        out["metadata"] = aws_sdk_qconnect.types.content_metadata.deserialize_json(
            data["metadata"]
        )
    if "externalSourceConfiguration" in data:
        import aws_sdk_qconnect.types.external_source_configuration

        out["external_source_configuration"] = (
            aws_sdk_qconnect.types.external_source_configuration.deserialize_json(
                data["externalSourceConfiguration"]
            )
        )
    return out
