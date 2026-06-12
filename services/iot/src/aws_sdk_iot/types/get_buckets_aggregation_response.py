"""Generated from Smithy shape ``com.amazonaws.iot#GetBucketsAggregationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.buckets
    import aws_sdk_iot.types.count


class GetBucketsAggregationResponse(TypedDict):
    total_count: "aws_sdk_iot.types.count.Count"
    """<p>The total number of things that fit the query string criteria.</p>"""
    buckets: NotRequired["aws_sdk_iot.types.buckets.Buckets"]
    """<p>The main part of the response with a list of buckets. Each bucket contains a <code>keyValue</code> and a <code>count</code>.</p> <p> <code>keyValue</code>: The aggregation field value counted for the particular bucket.</p> <p> <code>count</code>: The number of documents that have that value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBucketsAggregationResponse) -> dict:
    out: dict = {}
    out["totalCount"] = value.get("total_count", 0)
    if "buckets" in value:
        import aws_sdk_iot.types.buckets

        out["buckets"] = aws_sdk_iot.types.buckets.serialize_json(value["buckets"])
    return out


def deserialize_json(data: dict) -> GetBucketsAggregationResponse:
    out: GetBucketsAggregationResponse = {}  # type: ignore[typeddict-item]
    if "totalCount" in data:
        out["total_count"] = data["totalCount"]
    else:
        out["total_count"] = 0
    if "buckets" in data:
        import aws_sdk_iot.types.buckets

        out["buckets"] = aws_sdk_iot.types.buckets.deserialize_json(data["buckets"])
    return out
