"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteFolderMembershipResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DeleteFolderMembershipResponse(TypedDict):
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFolderMembershipResponse) -> dict:
    out: dict = {}
    out["Status"] = value.get("status", 0)
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DeleteFolderMembershipResponse:
    out: DeleteFolderMembershipResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        out["status"] = 0
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
