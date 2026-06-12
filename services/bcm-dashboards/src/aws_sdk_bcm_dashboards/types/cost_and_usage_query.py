"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#CostAndUsageQuery``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.date_time_range
    import aws_sdk_bcm_dashboards.types.expression
    import aws_sdk_bcm_dashboards.types.granularity
    import aws_sdk_bcm_dashboards.types.group_definitions
    import aws_sdk_bcm_dashboards.types.metric_names


class CostAndUsageQuery(TypedDict):
    metrics: "aws_sdk_bcm_dashboards.types.metric_names.MetricNames"
    """<p>The specific cost and usage metrics to retrieve.</p> <note> <p>Valid values for CostAndUsageQuery metrics are <code>AmortizedCost</code>, <code>BlendedCost</code>, <code>NetAmortizedCost</code>, <code>NetUnblendedCost</code>, <code>NormalizedUsageAmount</code>, <code>UnblendedCost</code>, and <code>UsageQuantity</code>.</p> </note>"""
    time_range: "aws_sdk_bcm_dashboards.types.date_time_range.DateTimeRange"
    """<p>The time period for which to retrieve data. Can be specified as absolute dates or relative time periods.</p>"""
    granularity: "aws_sdk_bcm_dashboards.types.granularity.Granularity"
    """<p>The granularity of the retrieved data: <code>HOURLY</code>, <code>DAILY</code>, or <code>MONTHLY</code>.</p>"""
    group_by: NotRequired[
        "aws_sdk_bcm_dashboards.types.group_definitions.GroupDefinitions"
    ]
    """<p>Specifies how to group the retrieved data, such as by <code>SERVICE</code>, <code>ACCOUNT</code>, or <code>TAG</code>.</p>"""
    filter: NotRequired["aws_sdk_bcm_dashboards.types.expression.Expression"]
    """<p>The filter expression to be applied to the cost and usage data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CostAndUsageQuery) -> dict:
    out: dict = {}
    import aws_sdk_bcm_dashboards.types.metric_names

    out["metrics"] = aws_sdk_bcm_dashboards.types.metric_names.serialize_aws_json_1_0(
        value["metrics"]
    )
    import aws_sdk_bcm_dashboards.types.date_time_range

    out["timeRange"] = (
        aws_sdk_bcm_dashboards.types.date_time_range.serialize_aws_json_1_0(
            value["time_range"]
        )
    )
    import aws_sdk_bcm_dashboards.types.granularity

    out["granularity"] = (
        aws_sdk_bcm_dashboards.types.granularity.serialize_aws_json_1_0(
            value["granularity"]
        )
    )
    if "group_by" in value:
        import aws_sdk_bcm_dashboards.types.group_definitions

        out["groupBy"] = (
            aws_sdk_bcm_dashboards.types.group_definitions.serialize_aws_json_1_0(
                value["group_by"]
            )
        )
    if "filter" in value:
        import aws_sdk_bcm_dashboards.types.expression

        out["filter"] = aws_sdk_bcm_dashboards.types.expression.serialize_aws_json_1_0(
            value["filter"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CostAndUsageQuery:
    out: CostAndUsageQuery = {}  # type: ignore[typeddict-item]
    if "metrics" in data:
        import aws_sdk_bcm_dashboards.types.metric_names

        out["metrics"] = (
            aws_sdk_bcm_dashboards.types.metric_names.deserialize_aws_json_1_0(
                data["metrics"]
            )
        )
    else:
        raise DeserializationError("CostAndUsageQuery.metrics required")
    if "timeRange" in data:
        import aws_sdk_bcm_dashboards.types.date_time_range

        out["time_range"] = (
            aws_sdk_bcm_dashboards.types.date_time_range.deserialize_aws_json_1_0(
                data["timeRange"]
            )
        )
    else:
        raise DeserializationError("CostAndUsageQuery.time_range required")
    if "granularity" in data:
        import aws_sdk_bcm_dashboards.types.granularity

        out["granularity"] = (
            aws_sdk_bcm_dashboards.types.granularity.deserialize_aws_json_1_0(
                data["granularity"]
            )
        )
    else:
        raise DeserializationError("CostAndUsageQuery.granularity required")
    if "groupBy" in data:
        import aws_sdk_bcm_dashboards.types.group_definitions

        out["group_by"] = (
            aws_sdk_bcm_dashboards.types.group_definitions.deserialize_aws_json_1_0(
                data["groupBy"]
            )
        )
    if "filter" in data:
        import aws_sdk_bcm_dashboards.types.expression

        out["filter"] = (
            aws_sdk_bcm_dashboards.types.expression.deserialize_aws_json_1_0(
                data["filter"]
            )
        )
    return out
