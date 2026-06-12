"""Generated from Smithy shape ``com.amazonaws.glue#UpdateJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class UpdateJobResponse(TypedDict):
    job_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Returns the name of the updated job definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateJobResponse) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateJobResponse:
    out: UpdateJobResponse = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    return out
