"""Generated from Smithy shape ``com.amazonaws.databrew#CreateProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.project_name


class CreateProjectResponse(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.project_name.ProjectName"
    """<p>The name of the project that you created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateProjectResponse:
    out: CreateProjectResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateProjectResponse.name required")
    return out
