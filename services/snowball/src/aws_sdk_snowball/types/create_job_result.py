"""Generated from Smithy shape ``com.amazonaws.snowball#CreateJobResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.job_id


class CreateJobResult(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_snowball.types.job_id.JobId"]
    """<p>The automatically generated ID for a job, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateJobResult) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateJobResult:
    out: CreateJobResult = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out
