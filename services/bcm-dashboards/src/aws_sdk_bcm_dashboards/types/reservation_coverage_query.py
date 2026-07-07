"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ReservationCoverageQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.date_time_range
    import aws_sdk_bcm_dashboards.types.expression
    import aws_sdk_bcm_dashboards.types.granularity
    import aws_sdk_bcm_dashboards.types.group_definitions
    import aws_sdk_bcm_dashboards.types.metric_names


class ReservationCoverageQuery(TypedDict, closed=True):
    time_range: "aws_sdk_bcm_dashboards.types.date_time_range.DateTimeRange"
    group_by: NotRequired[
        "aws_sdk_bcm_dashboards.types.group_definitions.GroupDefinitions"
    ]
    """<p>Specifies how to group the Reserved Instance coverage data, such as by service, Region, or instance type.</p>"""
    granularity: NotRequired["aws_sdk_bcm_dashboards.types.granularity.Granularity"]
    """<p>The time granularity of the retrieved data: <code>HOURLY</code>, <code>DAILY</code>, or <code>MONTHLY</code>.</p>"""
    filter: NotRequired["aws_sdk_bcm_dashboards.types.expression.Expression"]
    metrics: NotRequired["aws_sdk_bcm_dashboards.types.metric_names.MetricNames"]
    """<p>The coverage metrics to include in the results.</p> <note> <p>Valid values for ReservationCoverageQuery metrics are <code>Hour</code>, <code>Unit</code>, and <code>Cost</code>.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReservationCoverageQuery) -> dict:
    out: dict = {}
    import aws_sdk_bcm_dashboards.types.date_time_range

    out["timeRange"] = (
        aws_sdk_bcm_dashboards.types.date_time_range.serialize_aws_json_1_0(
            value["time_range"]
        )
    )
    if "group_by" in value:
        import aws_sdk_bcm_dashboards.types.group_definitions

        out["groupBy"] = (
            aws_sdk_bcm_dashboards.types.group_definitions.serialize_aws_json_1_0(
                value["group_by"]
            )
        )
    if "granularity" in value:
        import aws_sdk_bcm_dashboards.types.granularity

        out["granularity"] = (
            aws_sdk_bcm_dashboards.types.granularity.serialize_aws_json_1_0(
                value["granularity"]
            )
        )
    if "filter" in value:
        import aws_sdk_bcm_dashboards.types.expression

        out["filter"] = aws_sdk_bcm_dashboards.types.expression.serialize_aws_json_1_0(
            value["filter"]
        )
    if "metrics" in value:
        import aws_sdk_bcm_dashboards.types.metric_names

        out["metrics"] = (
            aws_sdk_bcm_dashboards.types.metric_names.serialize_aws_json_1_0(
                value["metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReservationCoverageQuery:
    out: ReservationCoverageQuery = {}  # type: ignore[typeddict-item]
    if "timeRange" in data:
        import aws_sdk_bcm_dashboards.types.date_time_range

        out["time_range"] = (
            aws_sdk_bcm_dashboards.types.date_time_range.deserialize_aws_json_1_0(
                data["timeRange"]
            )
        )
    else:
        raise DeserializationError("ReservationCoverageQuery.time_range required")
    if "groupBy" in data:
        import aws_sdk_bcm_dashboards.types.group_definitions

        out["group_by"] = (
            aws_sdk_bcm_dashboards.types.group_definitions.deserialize_aws_json_1_0(
                data["groupBy"]
            )
        )
    if "granularity" in data:
        import aws_sdk_bcm_dashboards.types.granularity

        out["granularity"] = (
            aws_sdk_bcm_dashboards.types.granularity.deserialize_aws_json_1_0(
                data["granularity"]
            )
        )
    if "filter" in data:
        import aws_sdk_bcm_dashboards.types.expression

        out["filter"] = (
            aws_sdk_bcm_dashboards.types.expression.deserialize_aws_json_1_0(
                data["filter"]
            )
        )
    if "metrics" in data:
        import aws_sdk_bcm_dashboards.types.metric_names

        out["metrics"] = (
            aws_sdk_bcm_dashboards.types.metric_names.deserialize_aws_json_1_0(
                data["metrics"]
            )
        )
    return out
