"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateFolderResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.restrictive_resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateFolderResponse(TypedDict):
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the folder.</p>"""
    folder_id: NotRequired[
        "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    ]
    """<p>The ID of the folder.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFolderResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "folder_id" in value:
        out["FolderId"] = value["folder_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateFolderResponse:
    out: UpdateFolderResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "FolderId" in data:
        out["folder_id"] = data["FolderId"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
