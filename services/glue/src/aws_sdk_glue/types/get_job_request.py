"""Generated from Smithy shape ``com.amazonaws.glue#GetJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class GetJobRequest(TypedDict):
    job_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the job definition to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobRequest:
    out: GetJobRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    else:
        raise DeserializationError("GetJobRequest.job_name required")
    return out
