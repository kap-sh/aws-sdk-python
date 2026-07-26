"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string


class GetProjectRequest(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProjectRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProjectRequest:
    out: GetProjectRequest = {}  # type: ignore[typeddict-item]
    return out
