"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#JobExecutionState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_jobs_data_plane.types.details_map
    import aws_sdk_iot_jobs_data_plane.types.job_execution_status
    import aws_sdk_iot_jobs_data_plane.types.version_number


class JobExecutionState(TypedDict):
    status: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.job_execution_status.JobExecutionStatus"
    ]
    r"""<p>The status of the job execution. Can be one of: \"QUEUED\", \"IN_PROGRESS\", \"FAILED\", \"SUCCESS\", \"CANCELED\", \"TIMED_OUT\", \"REJECTED\", or \"REMOVED\".</p>"""
    status_details: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.details_map.DetailsMap"
    ]
    """<p>A collection of name/value pairs that describe the status of the job execution.</p> <p>The maximum length of the value in the name/value pair is 1,024 characters.</p>"""
    version_number: "aws_sdk_iot_jobs_data_plane.types.version_number.VersionNumber"
    """<p>The version of the job execution. Job execution versions are incremented each time they are updated by a device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionState) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_iot_jobs_data_plane.types.job_execution_status

        out["status"] = (
            aws_sdk_iot_jobs_data_plane.types.job_execution_status.serialize_json(
                value["status"]
            )
        )
    if "status_details" in value:
        import aws_sdk_iot_jobs_data_plane.types.details_map

        out["statusDetails"] = (
            aws_sdk_iot_jobs_data_plane.types.details_map.serialize_json(
                value["status_details"]
            )
        )
    out["versionNumber"] = value.get("version_number", 0)
    return out


def deserialize_json(data: dict) -> JobExecutionState:
    out: JobExecutionState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_iot_jobs_data_plane.types.job_execution_status

        out["status"] = (
            aws_sdk_iot_jobs_data_plane.types.job_execution_status.deserialize_json(
                data["status"]
            )
        )
    if "statusDetails" in data:
        import aws_sdk_iot_jobs_data_plane.types.details_map

        out["status_details"] = (
            aws_sdk_iot_jobs_data_plane.types.details_map.deserialize_json(
                data["statusDetails"]
            )
        )
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    else:
        out["version_number"] = 0
    return out
