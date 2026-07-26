"""Generated from Smithy shape ``com.amazonaws.iot#GetBucketsAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.buckets
    import capo_iot.types.count


class GetBucketsAggregationResponse(TypedDict, closed=True):
    total_count: "capo_iot.types.count.Count"
    """<p>The total number of things that fit the query string criteria.</p>"""
    buckets: NotRequired["capo_iot.types.buckets.Buckets"]
    """<p>The main part of the response with a list of buckets. Each bucket contains a <code>keyValue</code> and a <code>count</code>.</p> <p> <code>keyValue</code>: The aggregation field value counted for the particular bucket.</p> <p> <code>count</code>: The number of documents that have that value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBucketsAggregationResponse) -> dict:
    out: dict = {}
    out["totalCount"] = value.get("total_count", 0)
    if "buckets" in value:
        import capo_iot.types.buckets

        out["buckets"] = capo_iot.types.buckets.serialize_json(value["buckets"])
    return out


def deserialize_json(data: dict) -> GetBucketsAggregationResponse:
    out: GetBucketsAggregationResponse = {}  # type: ignore[typeddict-item]
    if "totalCount" in data:
        out["total_count"] = data["totalCount"]
    else:
        out["total_count"] = 0
    if "buckets" in data:
        import capo_iot.types.buckets

        out["buckets"] = capo_iot.types.buckets.deserialize_json(data["buckets"])
    return out
