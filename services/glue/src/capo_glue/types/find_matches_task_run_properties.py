"""Generated from Smithy shape ``com.amazonaws.glue#FindMatchesTaskRunProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string
    import capo_glue.types.name_string


class FindMatchesTaskRunProperties(TypedDict, closed=True):
    job_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The job ID for the Find Matches task run.</p>"""
    job_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name assigned to the job for the Find Matches task run.</p>"""
    job_run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The job run ID for the Find Matches task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FindMatchesTaskRunProperties) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FindMatchesTaskRunProperties:
    out: FindMatchesTaskRunProperties = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobRunId" in data:
        out["job_run_id"] = data["JobRunId"]
    return out
