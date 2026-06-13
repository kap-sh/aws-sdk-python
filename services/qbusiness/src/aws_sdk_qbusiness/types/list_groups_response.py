"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.group_summary_list
    import aws_sdk_qbusiness.types.next_token


class ListGroupsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token that you can use in the subsequent request to retrieve the next set of groups that are mapped to users.</p>"""
    items: NotRequired["aws_sdk_qbusiness.types.group_summary_list.GroupSummaryList"]
    """<p>Summary information for list of groups that are mapped to users.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "items" in value:
        import aws_sdk_qbusiness.types.group_summary_list

        out["items"] = aws_sdk_qbusiness.types.group_summary_list.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> ListGroupsResponse:
    out: ListGroupsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "items" in data:
        import aws_sdk_qbusiness.types.group_summary_list

        out["items"] = aws_sdk_qbusiness.types.group_summary_list.deserialize_json(
            data["items"]
        )
    return out
