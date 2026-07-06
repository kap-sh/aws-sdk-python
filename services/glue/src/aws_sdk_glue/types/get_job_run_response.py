"""Generated from Smithy shape ``com.amazonaws.glue#GetJobRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.job_run


class GetJobRunResponse(TypedDict, closed=True):
    job_run: NotRequired["aws_sdk_glue.types.job_run.JobRun"]
    """<p>The requested job-run metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobRunResponse) -> dict:
    out: dict = {}
    if "job_run" in value:
        import aws_sdk_glue.types.job_run

        out["JobRun"] = aws_sdk_glue.types.job_run.serialize_aws_json_1_1(
            value["job_run"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobRunResponse:
    out: GetJobRunResponse = {}  # type: ignore[typeddict-item]
    if "JobRun" in data:
        import aws_sdk_glue.types.job_run

        out["job_run"] = aws_sdk_glue.types.job_run.deserialize_aws_json_1_1(
            data["JobRun"]
        )
    return out
