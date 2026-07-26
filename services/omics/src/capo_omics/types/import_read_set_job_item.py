"""Generated from Smithy shape ``com.amazonaws.omics#ImportReadSetJobItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.import_job_id
    import capo_omics.types.read_set_import_job_status
    import capo_omics.types.role_arn
    import capo_omics.types.sequence_store_id


class ImportReadSetJobItem(TypedDict, closed=True):
    id: "capo_omics.types.import_job_id.ImportJobId"
    """<p>The job's ID.</p>"""
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The job's sequence store ID.</p>"""
    role_arn: "capo_omics.types.role_arn.RoleArn"
    """<p>The job's service role ARN.</p>"""
    status: "capo_omics.types.read_set_import_job_status.ReadSetImportJobStatus"
    """<p>The job's status.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>When the job completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportReadSetJobItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["roleArn"] = value["role_arn"]
    out["status"] = value["status"]
    import capo_omics.types._prelude.timestamp

    out["creationTime"] = capo_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "completion_time" in value:
        import capo_omics.types._prelude.timestamp

        out["completionTime"] = capo_omics.types._prelude.timestamp.serialize_json(
            value["completion_time"]
        )
    return out


def deserialize_json(data: dict) -> ImportReadSetJobItem:
    out: ImportReadSetJobItem = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ImportReadSetJobItem.id required")
    if "sequenceStoreId" in data:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError("ImportReadSetJobItem.sequence_store_id required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("ImportReadSetJobItem.role_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ImportReadSetJobItem.status required")
    if "creationTime" in data:
        import capo_omics.types._prelude.timestamp

        out["creation_time"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("ImportReadSetJobItem.creation_time required")
    if "completionTime" in data:
        import capo_omics.types._prelude.timestamp

        out["completion_time"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["completionTime"]
        )
    return out
