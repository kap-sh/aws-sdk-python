"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeFolderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.folder
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeFolderResponse(TypedDict, closed=True):
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    folder: NotRequired["capo_quicksight.types.folder.Folder"]
    """<p>Information about the folder.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFolderResponse) -> dict:
    out: dict = {}
    if "folder" in value:
        import capo_quicksight.types.folder

        out["Folder"] = capo_quicksight.types.folder.serialize_json(value["folder"])
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeFolderResponse:
    out: DescribeFolderResponse = {}  # type: ignore[typeddict-item]
    if "Folder" in data:
        import capo_quicksight.types.folder

        out["folder"] = capo_quicksight.types.folder.deserialize_json(data["Folder"])
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
