"""Generated from Smithy shape ``com.amazonaws.inspector2#ListMembersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.list_members_max_results
    import aws_sdk_inspector2.types.next_token


class ListMembersRequest(TypedDict):
    only_associated: NotRequired["bool"]
    """<p>Specifies whether to list only currently associated members if <code>True</code> or to list all members within the organization if <code>False</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_inspector2.types.list_members_max_results.ListMembersMaxResults"
    ]
    """<p>The maximum number of results the response can return. If your request would return more than the maximum the response will return a <code>nextToken</code> value, use this value when you call the action again to get the remaining results.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. If your response returns more than the <code>maxResults</code> maximum value it will also return a <code>nextToken</code> value. For subsequent calls, use the <code>nextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembersRequest) -> dict:
    out: dict = {}
    if "only_associated" in value:
        out["onlyAssociated"] = value["only_associated"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMembersRequest:
    out: ListMembersRequest = {}  # type: ignore[typeddict-item]
    if "onlyAssociated" in data:
        out["only_associated"] = data["onlyAssociated"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
