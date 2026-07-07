"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxDataviewsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_dataviews
    import aws_sdk_finspace.types.pagination_token


class ListKxDataviewsResponse(TypedDict, closed=True):
    kx_dataviews: NotRequired["aws_sdk_finspace.types.kx_dataviews.KxDataviews"]
    """<p> The list of kdb dataviews that are currently active for the given database. </p>"""
    next_token: NotRequired["aws_sdk_finspace.types.pagination_token.PaginationToken"]
    """<p> A token that indicates where a results page should begin. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxDataviewsResponse) -> dict:
    out: dict = {}
    if "kx_dataviews" in value:
        import aws_sdk_finspace.types.kx_dataviews

        out["kxDataviews"] = aws_sdk_finspace.types.kx_dataviews.serialize_json(
            value["kx_dataviews"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKxDataviewsResponse:
    out: ListKxDataviewsResponse = {}  # type: ignore[typeddict-item]
    if "kxDataviews" in data:
        import aws_sdk_finspace.types.kx_dataviews

        out["kx_dataviews"] = aws_sdk_finspace.types.kx_dataviews.deserialize_json(
            data["kxDataviews"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
