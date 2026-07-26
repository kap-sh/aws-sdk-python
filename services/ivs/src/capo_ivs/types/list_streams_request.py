"""Generated from Smithy shape ``com.amazonaws.ivs#ListStreamsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.max_stream_results
    import capo_ivs.types.pagination_token
    import capo_ivs.types.stream_filters


class ListStreamsRequest(TypedDict, closed=True):
    filter_by: NotRequired["capo_ivs.types.stream_filters.StreamFilters"]
    """<p>Filters the stream list to match the specified criterion.</p>"""
    next_token: NotRequired["capo_ivs.types.pagination_token.PaginationToken"]
    """<p>The first stream to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired["capo_ivs.types.max_stream_results.MaxStreamResults"]
    """<p>Maximum number of streams to return. Default: 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamsRequest) -> dict:
    out: dict = {}
    if "filter_by" in value:
        import capo_ivs.types.stream_filters

        out["filterBy"] = capo_ivs.types.stream_filters.serialize_json(
            value["filter_by"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListStreamsRequest:
    out: ListStreamsRequest = {}  # type: ignore[typeddict-item]
    if "filterBy" in data:
        import capo_ivs.types.stream_filters

        out["filter_by"] = capo_ivs.types.stream_filters.deserialize_json(
            data["filterBy"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
