"""Generated from Smithy shape ``com.amazonaws.glue#JobNodeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.job_run_list


class JobNodeDetails(TypedDict, closed=True):
    job_runs: NotRequired["capo_glue.types.job_run_list.JobRunList"]
    """<p>The information for the job runs represented by the job node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobNodeDetails) -> dict:
    out: dict = {}
    if "job_runs" in value:
        import capo_glue.types.job_run_list

        out["JobRuns"] = capo_glue.types.job_run_list.serialize_aws_json_1_1(
            value["job_runs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JobNodeDetails:
    out: JobNodeDetails = {}  # type: ignore[typeddict-item]
    if "JobRuns" in data:
        import capo_glue.types.job_run_list

        out["job_runs"] = capo_glue.types.job_run_list.deserialize_aws_json_1_1(
            data["JobRuns"]
        )
    return out
