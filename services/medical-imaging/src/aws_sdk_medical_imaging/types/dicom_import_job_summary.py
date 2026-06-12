"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DICOMImportJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.date
    import aws_sdk_medical_imaging.types.job_id
    import aws_sdk_medical_imaging.types.job_name
    import aws_sdk_medical_imaging.types.job_status
    import aws_sdk_medical_imaging.types.message
    import aws_sdk_medical_imaging.types.role_arn


class DICOMImportJobSummary(TypedDict):
    job_id: "aws_sdk_medical_imaging.types.job_id.JobId"
    """<p>The import job identifier.</p>"""
    job_name: "aws_sdk_medical_imaging.types.job_name.JobName"
    """<p>The import job name.</p>"""
    job_status: "aws_sdk_medical_imaging.types.job_status.JobStatus"
    """<p>The filters for listing import jobs based on status.</p>"""
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    data_access_role_arn: NotRequired["aws_sdk_medical_imaging.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) that grants permissions to access medical imaging resources.</p>"""
    ended_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when an import job ended.</p>"""
    submitted_at: NotRequired["aws_sdk_medical_imaging.types.date.Date"]
    """<p>The timestamp when an import job was submitted.</p>"""
    message: NotRequired["aws_sdk_medical_imaging.types.message.Message"]
    """<p>The error message thrown if an import job fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DICOMImportJobSummary) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    out["jobName"] = value["job_name"]
    import aws_sdk_medical_imaging.types.job_status

    out["jobStatus"] = aws_sdk_medical_imaging.types.job_status.serialize_json(
        value["job_status"]
    )
    out["datastoreId"] = value["datastore_id"]
    if "data_access_role_arn" in value:
        out["dataAccessRoleArn"] = value["data_access_role_arn"]
    if "ended_at" in value:
        import aws_sdk_medical_imaging.types.date

        out["endedAt"] = aws_sdk_medical_imaging.types.date.serialize_json(
            value["ended_at"]
        )
    if "submitted_at" in value:
        import aws_sdk_medical_imaging.types.date

        out["submittedAt"] = aws_sdk_medical_imaging.types.date.serialize_json(
            value["submitted_at"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DICOMImportJobSummary:
    out: DICOMImportJobSummary = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("DICOMImportJobSummary.job_id required")
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("DICOMImportJobSummary.job_name required")
    if "jobStatus" in data:
        import aws_sdk_medical_imaging.types.job_status

        out["job_status"] = aws_sdk_medical_imaging.types.job_status.deserialize_json(
            data["jobStatus"]
        )
    else:
        raise DeserializationError("DICOMImportJobSummary.job_status required")
    if "datastoreId" in data:
        out["datastore_id"] = data["datastoreId"]
    else:
        raise DeserializationError("DICOMImportJobSummary.datastore_id required")
    if "dataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["dataAccessRoleArn"]
    if "endedAt" in data:
        import aws_sdk_medical_imaging.types.date

        out["ended_at"] = aws_sdk_medical_imaging.types.date.deserialize_json(
            data["endedAt"]
        )
    if "submittedAt" in data:
        import aws_sdk_medical_imaging.types.date

        out["submitted_at"] = aws_sdk_medical_imaging.types.date.deserialize_json(
            data["submittedAt"]
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
