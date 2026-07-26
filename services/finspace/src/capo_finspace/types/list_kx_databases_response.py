"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxDatabasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.kx_databases
    import capo_finspace.types.pagination_token


class ListKxDatabasesResponse(TypedDict, closed=True):
    kx_databases: NotRequired["capo_finspace.types.kx_databases.KxDatabases"]
    """<p>A list of databases in the kdb environment.</p>"""
    next_token: NotRequired["capo_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxDatabasesResponse) -> dict:
    out: dict = {}
    if "kx_databases" in value:
        import capo_finspace.types.kx_databases

        out["kxDatabases"] = capo_finspace.types.kx_databases.serialize_json(
            value["kx_databases"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKxDatabasesResponse:
    out: ListKxDatabasesResponse = {}  # type: ignore[typeddict-item]
    if "kxDatabases" in data:
        import capo_finspace.types.kx_databases

        out["kx_databases"] = capo_finspace.types.kx_databases.deserialize_json(
            data["kxDatabases"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
