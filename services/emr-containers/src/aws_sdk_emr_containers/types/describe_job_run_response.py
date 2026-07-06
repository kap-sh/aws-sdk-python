"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DescribeJobRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.job_run


class DescribeJobRunResponse(TypedDict, closed=True):
    job_run: NotRequired["aws_sdk_emr_containers.types.job_run.JobRun"]
    """<p>The output displays information about a job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobRunResponse) -> dict:
    out: dict = {}
    if "job_run" in value:
        import aws_sdk_emr_containers.types.job_run

        out["jobRun"] = aws_sdk_emr_containers.types.job_run.serialize_json(
            value["job_run"]
        )
    return out


def deserialize_json(data: dict) -> DescribeJobRunResponse:
    out: DescribeJobRunResponse = {}  # type: ignore[typeddict-item]
    if "jobRun" in data:
        import aws_sdk_emr_containers.types.job_run

        out["job_run"] = aws_sdk_emr_containers.types.job_run.deserialize_json(
            data["jobRun"]
        )
    return out
