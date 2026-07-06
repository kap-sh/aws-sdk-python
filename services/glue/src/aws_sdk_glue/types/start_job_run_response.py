"""Generated from Smithy shape ``com.amazonaws.glue#StartJobRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.id_string


class StartJobRunResponse(TypedDict, closed=True):
    job_run_id: NotRequired["aws_sdk_glue.types.id_string.IdString"]
    """<p>The ID assigned to this job run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartJobRunResponse) -> dict:
    out: dict = {}
    if "job_run_id" in value:
        out["JobRunId"] = value["job_run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartJobRunResponse:
    out: StartJobRunResponse = {}  # type: ignore[typeddict-item]
    if "JobRunId" in data:
        out["job_run_id"] = data["JobRunId"]
    return out
