"""Generated from Smithy shape ``com.amazonaws.glue#DeleteJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string


class DeleteJobResponse(TypedDict, closed=True):
    job_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the job definition that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteJobResponse) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteJobResponse:
    out: DeleteJobResponse = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    return out
