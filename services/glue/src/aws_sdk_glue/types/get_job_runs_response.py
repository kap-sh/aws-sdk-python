"""Generated from Smithy shape ``com.amazonaws.glue#GetJobRunsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.job_run_list


class GetJobRunsResponse(TypedDict):
    job_runs: NotRequired["aws_sdk_glue.types.job_run_list.JobRunList"]
    """<p>A list of job-run metadata objects.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if not all requested job runs have been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobRunsResponse) -> dict:
    out: dict = {}
    if "job_runs" in value:
        import aws_sdk_glue.types.job_run_list

        out["JobRuns"] = aws_sdk_glue.types.job_run_list.serialize_aws_json_1_1(
            value["job_runs"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobRunsResponse:
    out: GetJobRunsResponse = {}  # type: ignore[typeddict-item]
    if "JobRuns" in data:
        import aws_sdk_glue.types.job_run_list

        out["job_runs"] = aws_sdk_glue.types.job_run_list.deserialize_aws_json_1_1(
            data["JobRuns"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
