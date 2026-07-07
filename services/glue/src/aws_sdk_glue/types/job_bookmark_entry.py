"""Generated from Smithy shape ``com.amazonaws.glue#JobBookmarkEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.integer_value
    import aws_sdk_glue.types.job_name
    import aws_sdk_glue.types.json_value
    import aws_sdk_glue.types.run_id


class JobBookmarkEntry(TypedDict, closed=True):
    job_name: NotRequired["aws_sdk_glue.types.job_name.JobName"]
    """<p>The name of the job in question.</p>"""
    version: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>The version of the job.</p>"""
    run: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>The run ID number.</p>"""
    attempt: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>The attempt ID number.</p>"""
    previous_run_id: NotRequired["aws_sdk_glue.types.run_id.RunId"]
    """<p>The unique run identifier associated with the previous job run.</p>"""
    run_id: NotRequired["aws_sdk_glue.types.run_id.RunId"]
    """<p>The run ID number.</p>"""
    job_bookmark: NotRequired["aws_sdk_glue.types.json_value.JsonValue"]
    """<p>The bookmark itself.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobBookmarkEntry) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    out["Version"] = value.get("version", 0)
    out["Run"] = value.get("run", 0)
    out["Attempt"] = value.get("attempt", 0)
    if "previous_run_id" in value:
        out["PreviousRunId"] = value["previous_run_id"]
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "job_bookmark" in value:
        out["JobBookmark"] = value["job_bookmark"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobBookmarkEntry:
    out: JobBookmarkEntry = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if "Run" in data:
        out["run"] = data["Run"]
    else:
        out["run"] = 0
    if "Attempt" in data:
        out["attempt"] = data["Attempt"]
    else:
        out["attempt"] = 0
    if "PreviousRunId" in data:
        out["previous_run_id"] = data["PreviousRunId"]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "JobBookmark" in data:
        out["job_bookmark"] = data["JobBookmark"]
    return out
