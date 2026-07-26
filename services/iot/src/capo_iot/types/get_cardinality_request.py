"""Generated from Smithy shape ``com.amazonaws.iot#GetCardinalityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aggregation_field
    import capo_iot.types.index_name
    import capo_iot.types.query_string
    import capo_iot.types.query_version


class GetCardinalityRequest(TypedDict, closed=True):
    index_name: NotRequired["capo_iot.types.index_name.IndexName"]
    """<p>The name of the index to search.</p>"""
    query_string: "capo_iot.types.query_string.QueryString"
    """<p>The search query string.</p>"""
    aggregation_field: NotRequired["capo_iot.types.aggregation_field.AggregationField"]
    """<p>The field to aggregate.</p>"""
    query_version: NotRequired["capo_iot.types.query_version.QueryVersion"]
    """<p>The query version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCardinalityRequest) -> dict:
    out: dict = {}
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    out["queryString"] = value["query_string"]
    if "aggregation_field" in value:
        out["aggregationField"] = value["aggregation_field"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    return out


def deserialize_json(data: dict) -> GetCardinalityRequest:
    out: GetCardinalityRequest = {}  # type: ignore[typeddict-item]
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    else:
        raise DeserializationError("GetCardinalityRequest.query_string required")
    if "aggregationField" in data:
        out["aggregation_field"] = data["aggregationField"]
    if "queryVersion" in data:
        out["query_version"] = data["queryVersion"]
    return out
