"""Generated from Smithy shape ``com.amazonaws.iot#GetBucketsAggregationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aggregation_field
    import capo_iot.types.buckets_aggregation_type
    import capo_iot.types.index_name
    import capo_iot.types.query_string
    import capo_iot.types.query_version


class GetBucketsAggregationRequest(TypedDict, closed=True):
    index_name: NotRequired["capo_iot.types.index_name.IndexName"]
    """<p>The name of the index to search.</p>"""
    query_string: "capo_iot.types.query_string.QueryString"
    """<p>The search query string.</p>"""
    aggregation_field: "capo_iot.types.aggregation_field.AggregationField"
    """<p>The aggregation field.</p>"""
    query_version: NotRequired["capo_iot.types.query_version.QueryVersion"]
    """<p>The version of the query.</p>"""
    buckets_aggregation_type: (
        "capo_iot.types.buckets_aggregation_type.BucketsAggregationType"
    )
    """<p>The basic control of the response shape and the bucket aggregation type to perform. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBucketsAggregationRequest) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    out["queryString"] = value["query_string"]
    out["aggregationField"] = value["aggregation_field"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    import capo_iot.types.buckets_aggregation_type

    out["bucketsAggregationType"] = (
        capo_iot.types.buckets_aggregation_type.serialize_json(
            value["buckets_aggregation_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetBucketsAggregationRequest:
    out: GetBucketsAggregationRequest = {}  # type: ignore[typeddict-item]
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    else:
        raise DeserializationError("GetBucketsAggregationRequest.query_string required")
    if "aggregationField" in data:
        out["aggregation_field"] = data["aggregationField"]
    else:
        raise DeserializationError(
            "GetBucketsAggregationRequest.aggregation_field required"
        )
    if "queryVersion" in data:
        out["query_version"] = data["queryVersion"]
    if "bucketsAggregationType" in data:
        import capo_iot.types.buckets_aggregation_type

        out["buckets_aggregation_type"] = (
            capo_iot.types.buckets_aggregation_type.deserialize_json(
                data["bucketsAggregationType"]
            )
        )
    else:
        raise DeserializationError(
            "GetBucketsAggregationRequest.buckets_aggregation_type required"
        )
    return out
