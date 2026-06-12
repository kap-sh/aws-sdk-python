"""Generated from Smithy shape ``com.amazonaws.glue#DeleteJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class DeleteJobRequest(TypedDict):
    job_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the job definition to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteJobRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteJobRequest:
    out: DeleteJobRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    else:
        raise DeserializationError("DeleteJobRequest.job_name required")
    return out
