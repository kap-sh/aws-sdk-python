"""Generated from Smithy shape ``com.amazonaws.panorama#PackageImportJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_panorama.types.created_time
    import aws_sdk_panorama.types.job_id
    import aws_sdk_panorama.types.last_updated_time
    import aws_sdk_panorama.types.package_import_job_status
    import aws_sdk_panorama.types.package_import_job_status_message
    import aws_sdk_panorama.types.package_import_job_type


class PackageImportJob(TypedDict):
    job_id: NotRequired["aws_sdk_panorama.types.job_id.JobId"]
    """<p>The job's ID.</p>"""
    job_type: NotRequired[
        "aws_sdk_panorama.types.package_import_job_type.PackageImportJobType"
    ]
    """<p>The job's type.</p>"""
    status: NotRequired[
        "aws_sdk_panorama.types.package_import_job_status.PackageImportJobStatus"
    ]
    """<p>The job's status.</p>"""
    status_message: NotRequired[
        "aws_sdk_panorama.types.package_import_job_status_message.PackageImportJobStatusMessage"
    ]
    """<p>The job's status message.</p>"""
    created_time: NotRequired["aws_sdk_panorama.types.created_time.CreatedTime"]
    """<p>When the job was created.</p>"""
    last_updated_time: NotRequired[
        "aws_sdk_panorama.types.last_updated_time.LastUpdatedTime"
    ]
    """<p>When the job was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageImportJob) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_type" in value:
        out["JobType"] = value["job_type"]
    if "status" in value:
        out["Status"] = value["status"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "created_time" in value:
        import aws_sdk_panorama.types.created_time

        out["CreatedTime"] = aws_sdk_panorama.types.created_time.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_panorama.types.last_updated_time

        out["LastUpdatedTime"] = (
            aws_sdk_panorama.types.last_updated_time.serialize_json(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageImportJob:
    out: PackageImportJob = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "JobType" in data:
        out["job_type"] = data["JobType"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "CreatedTime" in data:
        import aws_sdk_panorama.types.created_time

        out["created_time"] = aws_sdk_panorama.types.created_time.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_panorama.types.last_updated_time

        out["last_updated_time"] = (
            aws_sdk_panorama.types.last_updated_time.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    return out
