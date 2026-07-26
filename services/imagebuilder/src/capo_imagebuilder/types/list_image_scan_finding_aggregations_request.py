"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListImageScanFindingAggregationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.filter
    import capo_imagebuilder.types.pagination_token


class ListImageScanFindingAggregationsRequest(TypedDict, closed=True):
    filter: NotRequired["capo_imagebuilder.types.filter.Filter"]
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImageScanFindingAggregationsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_imagebuilder.types.filter

        out["filter"] = capo_imagebuilder.types.filter.serialize_json(value["filter"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImageScanFindingAggregationsRequest:
    out: ListImageScanFindingAggregationsRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import capo_imagebuilder.types.filter

        out["filter"] = capo_imagebuilder.types.filter.deserialize_json(data["filter"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
