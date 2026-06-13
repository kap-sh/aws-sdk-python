"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateRoleCustomPermissionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateRoleCustomPermissionResponse(TypedDict):
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoleCustomPermissionResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    out["Status"] = value.get("status", 0)
    return out


def deserialize_json(data: dict) -> UpdateRoleCustomPermissionResponse:
    out: UpdateRoleCustomPermissionResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        out["status"] = 0
    return out
