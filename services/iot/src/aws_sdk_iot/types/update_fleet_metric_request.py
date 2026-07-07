"""Generated from Smithy shape ``com.amazonaws.iot#UpdateFleetMetricRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aggregation_field
    import aws_sdk_iot.types.aggregation_type
    import aws_sdk_iot.types.fleet_metric_description
    import aws_sdk_iot.types.fleet_metric_name
    import aws_sdk_iot.types.fleet_metric_period
    import aws_sdk_iot.types.fleet_metric_unit
    import aws_sdk_iot.types.index_name
    import aws_sdk_iot.types.optional_version
    import aws_sdk_iot.types.query_string
    import aws_sdk_iot.types.query_version


class UpdateFleetMetricRequest(TypedDict, closed=True):
    metric_name: "aws_sdk_iot.types.fleet_metric_name.FleetMetricName"
    """<p>The name of the fleet metric to update.</p>"""
    query_string: NotRequired["aws_sdk_iot.types.query_string.QueryString"]
    """<p>The search query string.</p>"""
    aggregation_type: NotRequired["aws_sdk_iot.types.aggregation_type.AggregationType"]
    """<p>The type of the aggregation query.</p>"""
    period: NotRequired["aws_sdk_iot.types.fleet_metric_period.FleetMetricPeriod"]
    """<p>The time in seconds between fleet metric emissions. Range [60(1 min), 86400(1 day)] and must be multiple of 60.</p>"""
    aggregation_field: NotRequired[
        "aws_sdk_iot.types.aggregation_field.AggregationField"
    ]
    """<p>The field to aggregate.</p>"""
    description: NotRequired[
        "aws_sdk_iot.types.fleet_metric_description.FleetMetricDescription"
    ]
    """<p>The description of the fleet metric.</p>"""
    query_version: NotRequired["aws_sdk_iot.types.query_version.QueryVersion"]
    """<p>The version of the query.</p>"""
    index_name: "aws_sdk_iot.types.index_name.IndexName"
    """<p>The name of the index to search.</p>"""
    unit: NotRequired["aws_sdk_iot.types.fleet_metric_unit.FleetMetricUnit"]
    r"""<p>Used to support unit transformation such as milliseconds to seconds. The unit must be supported by <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html\">CW metric</a>.</p>"""
    expected_version: NotRequired["aws_sdk_iot.types.optional_version.OptionalVersion"]
    """<p>The expected version of the fleet metric record in the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFleetMetricRequest) -> dict:
    out: dict = {}
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "aggregation_type" in value:
        import aws_sdk_iot.types.aggregation_type

        out["aggregationType"] = aws_sdk_iot.types.aggregation_type.serialize_json(
            value["aggregation_type"]
        )
    if "period" in value:
        out["period"] = value["period"]
    if "aggregation_field" in value:
        out["aggregationField"] = value["aggregation_field"]
    if "description" in value:
        out["description"] = value["description"]
    if "query_version" in value:
        out["queryVersion"] = value["query_version"]
    out["indexName"] = value["index_name"]
    if "unit" in value:
        import aws_sdk_iot.types.fleet_metric_unit

        out["unit"] = aws_sdk_iot.types.fleet_metric_unit.serialize_json(value["unit"])
    if "expected_version" in value:
        out["expectedVersion"] = value["expected_version"]
    return out


def deserialize_json(data: dict) -> UpdateFleetMetricRequest:
    out: UpdateFleetMetricRequest = {}  # type: ignore[typeddict-item]
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    if "aggregationType" in data:
        import aws_sdk_iot.types.aggregation_type

        out["aggregation_type"] = aws_sdk_iot.types.aggregation_type.deserialize_json(
            data["aggregationType"]
        )
    if "period" in data:
        out["period"] = data["period"]
    if "aggregationField" in data:
        out["aggregation_field"] = data["aggregationField"]
    if "description" in data:
        out["description"] = data["description"]
    if "queryVersion" in data:
        out["query_version"] = data["queryVersion"]
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    else:
        raise DeserializationError("UpdateFleetMetricRequest.index_name required")
    if "unit" in data:
        import aws_sdk_iot.types.fleet_metric_unit

        out["unit"] = aws_sdk_iot.types.fleet_metric_unit.deserialize_json(data["unit"])
    if "expectedVersion" in data:
        out["expected_version"] = data["expectedVersion"]
    return out
