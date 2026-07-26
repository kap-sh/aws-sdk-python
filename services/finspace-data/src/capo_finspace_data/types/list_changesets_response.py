"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListChangesetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.changeset_list
    import capo_finspace_data.types.pagination_token


class ListChangesetsResponse(TypedDict, closed=True):
    changesets: NotRequired["capo_finspace_data.types.changeset_list.ChangesetList"]
    """<p>List of Changesets found.</p>"""
    next_token: NotRequired["capo_finspace_data.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChangesetsResponse) -> dict:
    out: dict = {}
    if "changesets" in value:
        import capo_finspace_data.types.changeset_list

        out["changesets"] = capo_finspace_data.types.changeset_list.serialize_json(
            value["changesets"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChangesetsResponse:
    out: ListChangesetsResponse = {}  # type: ignore[typeddict-item]
    if "changesets" in data:
        import capo_finspace_data.types.changeset_list

        out["changesets"] = capo_finspace_data.types.changeset_list.deserialize_json(
            data["changesets"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
