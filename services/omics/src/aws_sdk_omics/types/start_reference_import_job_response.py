"""Generated from Smithy shape ``com.amazonaws.omics#StartReferenceImportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.import_job_id
    import aws_sdk_omics.types.reference_import_job_status
    import aws_sdk_omics.types.reference_store_id
    import aws_sdk_omics.types.role_arn


class StartReferenceImportJobResponse(TypedDict):
    id: "aws_sdk_omics.types.import_job_id.ImportJobId"
    """<p>The job's ID.</p>"""
    reference_store_id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The job's reference store ID.</p>"""
    role_arn: "aws_sdk_omics.types.role_arn.RoleArn"
    """<p>The job's service role ARN.</p>"""
    status: "aws_sdk_omics.types.reference_import_job_status.ReferenceImportJobStatus"
    """<p>The job's status.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReferenceImportJobResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["referenceStoreId"] = value["reference_store_id"]
    out["roleArn"] = value["role_arn"]
    out["status"] = value["status"]
    import aws_sdk_omics.types._prelude.timestamp

    out["creationTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> StartReferenceImportJobResponse:
    out: StartReferenceImportJobResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StartReferenceImportJobResponse.id required")
    if "referenceStoreId" in data:
        out["reference_store_id"] = data["referenceStoreId"]
    else:
        raise DeserializationError(
            "StartReferenceImportJobResponse.reference_store_id required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("StartReferenceImportJobResponse.role_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("StartReferenceImportJobResponse.status required")
    if "creationTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["creation_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "StartReferenceImportJobResponse.creation_time required"
        )
    return out
