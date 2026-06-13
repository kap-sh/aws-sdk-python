"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeFolderResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.folder
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeFolderResponse(TypedDict):
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    folder: NotRequired["aws_sdk_quicksight.types.folder.Folder"]
    """<p>Information about the folder.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFolderResponse) -> dict:
    out: dict = {}
    if "folder" in value:
        import aws_sdk_quicksight.types.folder

        out["Folder"] = aws_sdk_quicksight.types.folder.serialize_json(value["folder"])
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeFolderResponse:
    out: DescribeFolderResponse = {}  # type: ignore[typeddict-item]
    if "Folder" in data:
        import aws_sdk_quicksight.types.folder

        out["folder"] = aws_sdk_quicksight.types.folder.deserialize_json(data["Folder"])
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
