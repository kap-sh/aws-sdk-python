"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.group_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class SearchGroupsResponse(TypedDict, closed=True):
    group_list: NotRequired["aws_sdk_quicksight.types.group_list.GroupList"]
    """<p>A list of groups in a specified namespace that match the filters you set in your <code>SearchGroups</code> request.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchGroupsResponse) -> dict:
    out: dict = {}
    if "group_list" in value:
        import aws_sdk_quicksight.types.group_list

        out["GroupList"] = aws_sdk_quicksight.types.group_list.serialize_json(
            value["group_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchGroupsResponse:
    out: SearchGroupsResponse = {}  # type: ignore[typeddict-item]
    if "GroupList" in data:
        import aws_sdk_quicksight.types.group_list

        out["group_list"] = aws_sdk_quicksight.types.group_list.deserialize_json(
            data["GroupList"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
