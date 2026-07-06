"""Generated from Smithy shape ``com.amazonaws.quicksight#ListUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.user_list


class ListUsersResponse(TypedDict, closed=True):
    user_list: NotRequired["aws_sdk_quicksight.types.user_list.UserList"]
    """<p>The list of users.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersResponse) -> dict:
    out: dict = {}
    if "user_list" in value:
        import aws_sdk_quicksight.types.user_list

        out["UserList"] = aws_sdk_quicksight.types.user_list.serialize_json(
            value["user_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListUsersResponse:
    out: ListUsersResponse = {}  # type: ignore[typeddict-item]
    if "UserList" in data:
        import aws_sdk_quicksight.types.user_list

        out["user_list"] = aws_sdk_quicksight.types.user_list.deserialize_json(
            data["UserList"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
