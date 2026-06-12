"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxChangesetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_changesets
    import aws_sdk_finspace.types.pagination_token


class ListKxChangesetsResponse(TypedDict):
    kx_changesets: NotRequired["aws_sdk_finspace.types.kx_changesets.KxChangesets"]
    """<p>A list of changesets for a database.</p>"""
    next_token: NotRequired["aws_sdk_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxChangesetsResponse) -> dict:
    out: dict = {}
    if "kx_changesets" in value:
        import aws_sdk_finspace.types.kx_changesets

        out["kxChangesets"] = aws_sdk_finspace.types.kx_changesets.serialize_json(
            value["kx_changesets"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKxChangesetsResponse:
    out: ListKxChangesetsResponse = {}  # type: ignore[typeddict-item]
    if "kxChangesets" in data:
        import aws_sdk_finspace.types.kx_changesets

        out["kx_changesets"] = aws_sdk_finspace.types.kx_changesets.deserialize_json(
            data["kxChangesets"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
