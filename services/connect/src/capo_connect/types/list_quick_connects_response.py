"""Generated from Smithy shape ``com.amazonaws.connect#ListQuickConnectsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.quick_connect_summary_list


class ListQuickConnectsResponse(TypedDict, closed=True):
    quick_connect_summary_list: NotRequired[
        "capo_connect.types.quick_connect_summary_list.QuickConnectSummaryList"
    ]
    """<p>Information about the quick connects.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQuickConnectsResponse) -> dict:
    out: dict = {}
    if "quick_connect_summary_list" in value:
        import capo_connect.types.quick_connect_summary_list

        out["QuickConnectSummaryList"] = (
            capo_connect.types.quick_connect_summary_list.serialize_json(
                value["quick_connect_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQuickConnectsResponse:
    out: ListQuickConnectsResponse = {}  # type: ignore[typeddict-item]
    if "QuickConnectSummaryList" in data:
        import capo_connect.types.quick_connect_summary_list

        out["quick_connect_summary_list"] = (
            capo_connect.types.quick_connect_summary_list.deserialize_json(
                data["QuickConnectSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
