"""Generated from Smithy shape ``com.amazonaws.workdocs#GetFolderPathResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.resource_path


class GetFolderPathResponse(TypedDict, closed=True):
    path: NotRequired["capo_workdocs.types.resource_path.ResourcePath"]
    """<p>The path information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFolderPathResponse) -> dict:
    out: dict = {}
    if "path" in value:
        import capo_workdocs.types.resource_path

        out["Path"] = capo_workdocs.types.resource_path.serialize_json(value["path"])
    return out


def deserialize_json(data: dict) -> GetFolderPathResponse:
    out: GetFolderPathResponse = {}  # type: ignore[typeddict-item]
    if "Path" in data:
        import capo_workdocs.types.resource_path

        out["path"] = capo_workdocs.types.resource_path.deserialize_json(data["Path"])
    return out
