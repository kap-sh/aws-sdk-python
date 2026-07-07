"""Generated from Smithy shape ``com.amazonaws.glue#UpdateSourceControlFromJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class UpdateSourceControlFromJobResponse(TypedDict, closed=True):
    job_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the Glue job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSourceControlFromJobResponse) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSourceControlFromJobResponse:
    out: UpdateSourceControlFromJobResponse = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    return out
