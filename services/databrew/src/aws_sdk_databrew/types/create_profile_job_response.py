"""Generated from Smithy shape ``com.amazonaws.databrew#CreateProfileJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.job_name


class CreateProfileJobResponse(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.job_name.JobName"
    """<p>The name of the job that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProfileJobResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateProfileJobResponse:
    out: CreateProfileJobResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateProfileJobResponse.name required")
    return out
