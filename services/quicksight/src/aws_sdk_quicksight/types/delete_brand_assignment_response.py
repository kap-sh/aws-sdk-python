"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteBrandAssignmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string


class DeleteBrandAssignmentResponse(TypedDict):
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrandAssignmentResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DeleteBrandAssignmentResponse:
    out: DeleteBrandAssignmentResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
