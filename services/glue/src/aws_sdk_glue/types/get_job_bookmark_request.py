"""Generated from Smithy shape ``com.amazonaws.glue#GetJobBookmarkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.job_name
    import aws_sdk_glue.types.run_id


class GetJobBookmarkRequest(TypedDict, closed=True):
    job_name: "aws_sdk_glue.types.job_name.JobName"
    """<p>The name of the job in question.</p>"""
    run_id: NotRequired["aws_sdk_glue.types.run_id.RunId"]
    """<p>The unique run identifier associated with this job run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobBookmarkRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobBookmarkRequest:
    out: GetJobBookmarkRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    else:
        raise DeserializationError("GetJobBookmarkRequest.job_name required")
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    return out
