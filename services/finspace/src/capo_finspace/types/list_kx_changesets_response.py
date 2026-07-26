"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxChangesetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.kx_changesets
    import capo_finspace.types.pagination_token


class ListKxChangesetsResponse(TypedDict, closed=True):
    kx_changesets: NotRequired["capo_finspace.types.kx_changesets.KxChangesets"]
    """<p>A list of changesets for a database.</p>"""
    next_token: NotRequired["capo_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxChangesetsResponse) -> dict:
    out: dict = {}
    if "kx_changesets" in value:
        import capo_finspace.types.kx_changesets

        out["kxChangesets"] = capo_finspace.types.kx_changesets.serialize_json(
            value["kx_changesets"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKxChangesetsResponse:
    out: ListKxChangesetsResponse = {}  # type: ignore[typeddict-item]
    if "kxChangesets" in data:
        import capo_finspace.types.kx_changesets

        out["kx_changesets"] = capo_finspace.types.kx_changesets.deserialize_json(
            data["kxChangesets"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
