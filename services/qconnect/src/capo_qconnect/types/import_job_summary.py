"""Generated from Smithy shape ``com.amazonaws.qconnect#ImportJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.arn
    import capo_qconnect.types.content_metadata
    import capo_qconnect.types.external_source_configuration
    import capo_qconnect.types.import_job_status
    import capo_qconnect.types.import_job_type
    import capo_qconnect.types.upload_id
    import capo_qconnect.types.uuid


class ImportJobSummary(TypedDict, closed=True):
    import_job_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the import job.</p>"""
    knowledge_base_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the knowledge base.</p>"""
    upload_id: "capo_qconnect.types.upload_id.UploadId"
    r"""<p>A pointer to the uploaded asset. This value is returned by <a href=\"https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html\">StartContentUpload</a>.</p>"""
    knowledge_base_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    import_job_type: "capo_qconnect.types.import_job_type.ImportJobType"
    """<p>The type of import job.</p>"""
    status: "capo_qconnect.types.import_job_status.ImportJobStatus"
    """<p>The status of the import job.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the import job was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp when the import job was last modified.</p>"""
    metadata: NotRequired["capo_qconnect.types.content_metadata.ContentMetadata"]
    """<p>The metadata fields of the imported Amazon Q in Connect resources.</p>"""
    external_source_configuration: NotRequired[
        "capo_qconnect.types.external_source_configuration.ExternalSourceConfiguration"
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
    import capo_qconnect.types._prelude.timestamp

    out["createdTime"] = capo_qconnect.types._prelude.timestamp.serialize_json(
        value["created_time"]
    )
    import capo_qconnect.types._prelude.timestamp

    out["lastModifiedTime"] = capo_qconnect.types._prelude.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "metadata" in value:
        import capo_qconnect.types.content_metadata

        out["metadata"] = capo_qconnect.types.content_metadata.serialize_json(
            value["metadata"]
        )
    if "external_source_configuration" in value:
        import capo_qconnect.types.external_source_configuration

        out["externalSourceConfiguration"] = (
            capo_qconnect.types.external_source_configuration.serialize_json(
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
        import capo_qconnect.types._prelude.timestamp

        out["created_time"] = capo_qconnect.types._prelude.timestamp.deserialize_json(
            data["createdTime"]
        )
    else:
        raise DeserializationError("ImportJobSummary.created_time required")
    if "lastModifiedTime" in data:
        import capo_qconnect.types._prelude.timestamp

        out["last_modified_time"] = (
            capo_qconnect.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("ImportJobSummary.last_modified_time required")
    if "metadata" in data:
        import capo_qconnect.types.content_metadata

        out["metadata"] = capo_qconnect.types.content_metadata.deserialize_json(
            data["metadata"]
        )
    if "externalSourceConfiguration" in data:
        import capo_qconnect.types.external_source_configuration

        out["external_source_configuration"] = (
            capo_qconnect.types.external_source_configuration.deserialize_json(
                data["externalSourceConfiguration"]
            )
        )
    return out
