"""Generated from Smithy shape ``com.amazonaws.codecatalyst#UpdateProjectRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.project_description


class UpdateProjectRequest(TypedDict):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project.</p>"""
    description: NotRequired[
        "aws_sdk_codecatalyst.types.project_description.ProjectDescription"
    ]
    """<p>The description of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProjectRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateProjectRequest:
    out: UpdateProjectRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    return out
