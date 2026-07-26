"""Generated from Smithy shape ``com.amazonaws.omics#GetReadSetImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.import_job_id
    import capo_omics.types.import_read_set_source_list
    import capo_omics.types.job_status_message
    import capo_omics.types.read_set_import_job_status
    import capo_omics.types.role_arn
    import capo_omics.types.sequence_store_id


class GetReadSetImportJobResponse(TypedDict, closed=True):
    id: "capo_omics.types.import_job_id.ImportJobId"
    """<p>The job's ID.</p>"""
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The job's sequence store ID.</p>"""
    role_arn: "capo_omics.types.role_arn.RoleArn"
    """<p>The job's service role ARN.</p>"""
    status: "capo_omics.types.read_set_import_job_status.ReadSetImportJobStatus"
    """<p>The job's status.</p>"""
    status_message: NotRequired["capo_omics.types.job_status_message.JobStatusMessage"]
    """<p>The job's status message.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>When the job completed.</p>"""
    sources: "capo_omics.types.import_read_set_source_list.ImportReadSetSourceList"
    """<p>The job's source files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadSetImportJobResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["roleArn"] = value["role_arn"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    import capo_omics.types._prelude.timestamp

    out["creationTime"] = capo_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "completion_time" in value:
        import capo_omics.types._prelude.timestamp

        out["completionTime"] = capo_omics.types._prelude.timestamp.serialize_json(
            value["completion_time"]
        )
    import capo_omics.types.import_read_set_source_list

    out["sources"] = capo_omics.types.import_read_set_source_list.serialize_json(
        value["sources"]
    )
    return out


def deserialize_json(data: dict) -> GetReadSetImportJobResponse:
    out: GetReadSetImportJobResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetReadSetImportJobResponse.id required")
    if "sequenceStoreId" in data:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError(
            "GetReadSetImportJobResponse.sequence_store_id required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GetReadSetImportJobResponse.role_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetReadSetImportJobResponse.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "creationTime" in data:
        import capo_omics.types._prelude.timestamp

        out["creation_time"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("GetReadSetImportJobResponse.creation_time required")
    if "completionTime" in data:
        import capo_omics.types._prelude.timestamp

        out["completion_time"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["completionTime"]
        )
    if "sources" in data:
        import capo_omics.types.import_read_set_source_list

        out["sources"] = capo_omics.types.import_read_set_source_list.deserialize_json(
            data["sources"]
        )
    else:
        raise DeserializationError("GetReadSetImportJobResponse.sources required")
    return out
