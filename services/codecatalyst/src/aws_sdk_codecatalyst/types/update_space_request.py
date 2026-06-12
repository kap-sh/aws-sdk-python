"""Generated from Smithy shape ``com.amazonaws.codecatalyst#UpdateSpaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.space_description


class UpdateSpaceRequest(TypedDict):
    name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    description: NotRequired[
        "aws_sdk_codecatalyst.types.space_description.SpaceDescription"
    ]
    """<p>The description of the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSpaceRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateSpaceRequest:
    out: UpdateSpaceRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    return out
