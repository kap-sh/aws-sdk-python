"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CreateProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.project_description
    import aws_sdk_codecatalyst.types.project_display_name


class CreateProjectRequest(TypedDict, closed=True):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    display_name: "aws_sdk_codecatalyst.types.project_display_name.ProjectDisplayName"
    """<p>The friendly name of the project that will be displayed to users.</p>"""
    description: NotRequired[
        "aws_sdk_codecatalyst.types.project_description.ProjectDescription"
    ]
    """<p>The description of the project. This description will be displayed to all users of the project. We recommend providing a brief description of the project and its intended purpose.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateProjectRequest:
    out: CreateProjectRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateProjectRequest.display_name required")
    if "description" in data:
        out["description"] = data["description"]
    return out
