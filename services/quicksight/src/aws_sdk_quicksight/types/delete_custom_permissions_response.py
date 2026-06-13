"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteCustomPermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DeleteCustomPermissionsResponse(TypedDict):
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the custom permissions profile.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomPermissionsResponse) -> dict:
    out: dict = {}
    out["Status"] = value.get("status", 0)
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DeleteCustomPermissionsResponse:
    out: DeleteCustomPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        out["status"] = 0
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
