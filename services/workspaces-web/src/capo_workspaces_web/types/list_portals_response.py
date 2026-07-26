"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListPortalsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.pagination_token
    import capo_workspaces_web.types.portal_list


class ListPortalsResponse(TypedDict, closed=True):
    portals: NotRequired["capo_workspaces_web.types.portal_list.PortalList"]
    """<p>The portals in the list.</p>"""
    next_token: NotRequired[
        "capo_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPortalsResponse) -> dict:
    out: dict = {}
    if "portals" in value:
        import capo_workspaces_web.types.portal_list

        out["portals"] = capo_workspaces_web.types.portal_list.serialize_json(
            value["portals"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPortalsResponse:
    out: ListPortalsResponse = {}  # type: ignore[typeddict-item]
    if "portals" in data:
        import capo_workspaces_web.types.portal_list

        out["portals"] = capo_workspaces_web.types.portal_list.deserialize_json(
            data["portals"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
