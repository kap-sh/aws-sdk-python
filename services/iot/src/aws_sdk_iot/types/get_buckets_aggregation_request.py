"""Generated from Smithy shape ``com.amazonaws.iot#GetBucketsAggregationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aggregation_field
    import aws_sdk_iot.types.buckets_aggregation_type
    import aws_sdk_iot.types.index_name
    import aws_sdk_iot.types.query_string
    import aws_sdk_iot.types.query_version


class GetBucketsAggregationRequest(TypedDict):
    index_name: NotRequired["aws_sdk_iot.types.index_name.IndexName"]
    """<p>The name of the index to search.</p>"""
    query_string: "aws_sdk_iot.types.query_string.QueryString"
    """<p>The search query string.</p>"""
    aggregation_field: "aws_sdk_iot.types.aggregation_field.AggregationField"
    """<p>The aggregation field.</p>"""
    query_version: NotRequired["aws_sdk_iot.types.query_version.QueryVersion"]
    """<p>The version of the query.</p>"""
    buckets_aggregation_type: (
        "aws_sdk_iot.types.buckets_aggregation_type.BucketsAggregationType"
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
    import aws_sdk_iot.types.buckets_aggregation_type

    out["bucketsAggregationType"] = (
        aws_sdk_iot.types.buckets_aggregation_type.serialize_json(
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
        import aws_sdk_iot.types.buckets_aggregation_type

        out["buckets_aggregation_type"] = (
            aws_sdk_iot.types.buckets_aggregation_type.deserialize_json(
                data["bucketsAggregationType"]
            )
        )
    else:
        raise DeserializationError(
            "GetBucketsAggregationRequest.buckets_aggregation_type required"
        )
    return out
