"""Generated from Smithy shape ``com.amazonaws.codecatalyst#UpdateSpaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.space_description


class UpdateSpaceRequest(TypedDict, closed=True):
    name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    description: NotRequired[
        "capo_codecatalyst.types.space_description.SpaceDescription"
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
