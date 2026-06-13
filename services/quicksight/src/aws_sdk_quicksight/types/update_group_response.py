"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.group
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateGroupResponse(TypedDict):
    group: NotRequired["aws_sdk_quicksight.types.group.Group"]
    """<p>The name of the group.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupResponse) -> dict:
    out: dict = {}
    if "group" in value:
        import aws_sdk_quicksight.types.group

        out["Group"] = aws_sdk_quicksight.types.group.serialize_json(value["group"])
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateGroupResponse:
    out: UpdateGroupResponse = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        import aws_sdk_quicksight.types.group

        out["group"] = aws_sdk_quicksight.types.group.deserialize_json(data["Group"])
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
