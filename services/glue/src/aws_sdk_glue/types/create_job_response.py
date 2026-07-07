"""Generated from Smithy shape ``com.amazonaws.glue#CreateJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class CreateJobResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The unique name that was provided for this job definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateJobResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateJobResponse:
    out: CreateJobResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
