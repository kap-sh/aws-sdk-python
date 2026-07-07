"""Generated from Smithy shape ``com.amazonaws.xray#GetGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.group_summary_list
    import aws_sdk_xray.types.string


class GetGroupsResult(TypedDict, closed=True):
    groups: NotRequired["aws_sdk_xray.types.group_summary_list.GroupSummaryList"]
    """<p>The collection of all active groups.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupsResult) -> dict:
    out: dict = {}
    if "groups" in value:
        import aws_sdk_xray.types.group_summary_list

        out["Groups"] = aws_sdk_xray.types.group_summary_list.serialize_json(
            value["groups"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetGroupsResult:
    out: GetGroupsResult = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import aws_sdk_xray.types.group_summary_list

        out["groups"] = aws_sdk_xray.types.group_summary_list.deserialize_json(
            data["Groups"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
