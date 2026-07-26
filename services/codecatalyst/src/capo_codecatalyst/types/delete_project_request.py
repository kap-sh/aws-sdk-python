"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DeleteProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string


class DeleteProjectRequest(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space. To retrieve a list of project names, use <a>ListProjects</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProjectRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProjectRequest:
    out: DeleteProjectRequest = {}  # type: ignore[typeddict-item]
    return out
