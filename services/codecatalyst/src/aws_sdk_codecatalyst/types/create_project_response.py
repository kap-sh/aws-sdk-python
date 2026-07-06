"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CreateProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string


class CreateProjectResponse(TypedDict, closed=True):
    space_name: NotRequired["aws_sdk_codecatalyst.types.name_string.NameString"]
    """<p>The name of the space.</p>"""
    name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    display_name: NotRequired["str"]
    """<p>The friendly name of the project.</p>"""
    description: NotRequired["str"]
    """<p>The description of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectResponse) -> dict:
    out: dict = {}
    if "space_name" in value:
        out["spaceName"] = value["space_name"]
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateProjectResponse:
    out: CreateProjectResponse = {}  # type: ignore[typeddict-item]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateProjectResponse.name required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    return out
