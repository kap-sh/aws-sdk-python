"""Generated from Smithy shape ``com.amazonaws.omics#StartReadSetImportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.import_job_id
    import aws_sdk_omics.types.read_set_import_job_status
    import aws_sdk_omics.types.role_arn
    import aws_sdk_omics.types.sequence_store_id


class StartReadSetImportJobResponse(TypedDict):
    id: "aws_sdk_omics.types.import_job_id.ImportJobId"
    """<p>The job's ID.</p>"""
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read set's sequence store ID.</p>"""
    role_arn: "aws_sdk_omics.types.role_arn.RoleArn"
    """<p>The job's service role ARN.</p>"""
    status: "aws_sdk_omics.types.read_set_import_job_status.ReadSetImportJobStatus"
    """<p>The job's status.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReadSetImportJobResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["roleArn"] = value["role_arn"]
    out["status"] = value["status"]
    import aws_sdk_omics.types._prelude.timestamp

    out["creationTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> StartReadSetImportJobResponse:
    out: StartReadSetImportJobResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StartReadSetImportJobResponse.id required")
    if "sequenceStoreId" in data:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError(
            "StartReadSetImportJobResponse.sequence_store_id required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("StartReadSetImportJobResponse.role_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("StartReadSetImportJobResponse.status required")
    if "creationTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["creation_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "StartReadSetImportJobResponse.creation_time required"
        )
    return out
