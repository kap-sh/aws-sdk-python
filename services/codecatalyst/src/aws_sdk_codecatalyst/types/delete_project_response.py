"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DeleteProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string


class DeleteProjectResponse(TypedDict, closed=True):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    display_name: NotRequired["str"]
    """<p>The friendly name displayed to users of the project in Amazon CodeCatalyst.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProjectResponse) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> DeleteProjectResponse:
    out: DeleteProjectResponse = {}  # type: ignore[typeddict-item]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError("DeleteProjectResponse.space_name required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteProjectResponse.name required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    return out
