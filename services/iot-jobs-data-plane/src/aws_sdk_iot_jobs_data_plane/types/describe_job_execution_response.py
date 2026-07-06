"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#DescribeJobExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_jobs_data_plane.types.job_execution


class DescribeJobExecutionResponse(TypedDict, closed=True):
    execution: NotRequired[
        "aws_sdk_iot_jobs_data_plane.types.job_execution.JobExecution"
    ]
    """<p>Contains data about a job execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobExecutionResponse) -> dict:
    out: dict = {}
    if "execution" in value:
        import aws_sdk_iot_jobs_data_plane.types.job_execution

        out["execution"] = (
            aws_sdk_iot_jobs_data_plane.types.job_execution.serialize_json(
                value["execution"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeJobExecutionResponse:
    out: DescribeJobExecutionResponse = {}  # type: ignore[typeddict-item]
    if "execution" in data:
        import aws_sdk_iot_jobs_data_plane.types.job_execution

        out["execution"] = (
            aws_sdk_iot_jobs_data_plane.types.job_execution.deserialize_json(
                data["execution"]
            )
        )
    return out
