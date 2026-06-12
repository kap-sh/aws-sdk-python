"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteProjectResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.project_name


class DeleteProjectResponse(TypedDict):
    name: "aws_sdk_databrew.types.project_name.ProjectName"
    """<p>The name of the project that you deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProjectResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteProjectResponse:
    out: DeleteProjectResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteProjectResponse.name required")
    return out
