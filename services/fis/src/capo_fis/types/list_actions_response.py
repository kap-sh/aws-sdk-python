"""Generated from Smithy shape ``com.amazonaws.fis#ListActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.action_summary_list
    import capo_fis.types.next_token


class ListActionsResponse(TypedDict, closed=True):
    actions: NotRequired["capo_fis.types.action_summary_list.ActionSummaryList"]
    """<p>The actions.</p>"""
    next_token: NotRequired["capo_fis.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActionsResponse) -> dict:
    out: dict = {}
    if "actions" in value:
        import capo_fis.types.action_summary_list

        out["actions"] = capo_fis.types.action_summary_list.serialize_json(
            value["actions"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListActionsResponse:
    out: ListActionsResponse = {}  # type: ignore[typeddict-item]
    if "actions" in data:
        import capo_fis.types.action_summary_list

        out["actions"] = capo_fis.types.action_summary_list.deserialize_json(
            data["actions"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
