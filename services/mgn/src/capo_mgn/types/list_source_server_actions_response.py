"""Generated from Smithy shape ``com.amazonaws.mgn#ListSourceServerActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.pagination_token
    import capo_mgn.types.source_server_action_documents


class ListSourceServerActionsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mgn.types.source_server_action_documents.SourceServerActionDocuments"
    ]
    """<p>List of source server post migration custom actions.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>Next token returned when listing source server post migration custom actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceServerActionsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.source_server_action_documents

        out["items"] = capo_mgn.types.source_server_action_documents.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSourceServerActionsResponse:
    out: ListSourceServerActionsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_mgn.types.source_server_action_documents

        out["items"] = capo_mgn.types.source_server_action_documents.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
