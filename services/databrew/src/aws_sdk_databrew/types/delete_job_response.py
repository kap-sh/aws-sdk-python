"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.job_name


class DeleteJobResponse(TypedDict):
    name: "aws_sdk_databrew.types.job_name.JobName"
    """<p>The name of the job that you deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteJobResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteJobResponse:
    out: DeleteJobResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteJobResponse.name required")
    return out
