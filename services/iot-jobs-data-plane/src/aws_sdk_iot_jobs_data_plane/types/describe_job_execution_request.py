"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#DescribeJobExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_jobs_data_plane.types.describe_job_execution_job_id
    import aws_sdk_iot_jobs_data_plane.types.execution_number
    import aws_sdk_iot_jobs_data_plane.types.include_job_document
    import aws_sdk_iot_jobs_data_plane.types.thing_name


class DescribeJobExecutionRequest(TypedDict, closed=True):
    job_id: "aws_sdk_iot_jobs_data_plane.types.describe_job_execution_job_id.DescribeJobExecutionJobId"
    """<p>The unique identifier assigned to this job when it was created.</p>"""
    thing_name: "aws_sdk_iot_jobs_data_plane.types.thing_name.ThingName"
    """<p>The thing name associated with the device the job execution is running on.</p>"""
    include_job_document: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.include_job_document.IncludeJobDocument"
    ]
    """<p>Optional. Unless set to false, the response contains the job document. The default is true.</p>"""
    execution_number: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.execution_number.ExecutionNumber"
    ]
    """<p>Optional. A number that identifies a particular job execution on a particular device. If not specified, the latest job execution is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeJobExecutionRequest:
    out: DescribeJobExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
