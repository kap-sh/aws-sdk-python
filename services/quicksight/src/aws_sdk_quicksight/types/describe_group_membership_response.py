"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeGroupMembershipResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.group_member
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeGroupMembershipResponse(TypedDict):
    group_member: NotRequired["aws_sdk_quicksight.types.group_member.GroupMember"]
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGroupMembershipResponse) -> dict:
    out: dict = {}
    if "group_member" in value:
        import aws_sdk_quicksight.types.group_member

        out["GroupMember"] = aws_sdk_quicksight.types.group_member.serialize_json(
            value["group_member"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeGroupMembershipResponse:
    out: DescribeGroupMembershipResponse = {}  # type: ignore[typeddict-item]
    if "GroupMember" in data:
        import aws_sdk_quicksight.types.group_member

        out["group_member"] = aws_sdk_quicksight.types.group_member.deserialize_json(
            data["GroupMember"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
