"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#SavingsPlansCoverageQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.date_time_range
    import capo_bcm_dashboards.types.expression
    import capo_bcm_dashboards.types.granularity
    import capo_bcm_dashboards.types.group_definitions
    import capo_bcm_dashboards.types.metric_names


class SavingsPlansCoverageQuery(TypedDict, closed=True):
    time_range: "capo_bcm_dashboards.types.date_time_range.DateTimeRange"
    metrics: NotRequired["capo_bcm_dashboards.types.metric_names.MetricNames"]
    """<p>The coverage metrics to include in the results.</p> <note> <p>Valid value for SavingsPlansCoverageQuery metrics is <code>SpendCoveredBySavingsPlans</code>.</p> </note>"""
    granularity: NotRequired["capo_bcm_dashboards.types.granularity.Granularity"]
    """<p>The time granularity of the retrieved data: <code>HOURLY</code>, <code>DAILY</code>, or <code>MONTHLY</code>.</p>"""
    group_by: NotRequired[
        "capo_bcm_dashboards.types.group_definitions.GroupDefinitions"
    ]
    """<p>Specifies how to group the Savings Plans coverage data, such as by service or instance family.</p>"""
    filter: NotRequired["capo_bcm_dashboards.types.expression.Expression"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SavingsPlansCoverageQuery) -> dict:
    out: dict = {}
    import capo_bcm_dashboards.types.date_time_range

    out["timeRange"] = capo_bcm_dashboards.types.date_time_range.serialize_aws_json_1_0(
        value["time_range"]
    )
    if "metrics" in value:
        import capo_bcm_dashboards.types.metric_names

        out["metrics"] = capo_bcm_dashboards.types.metric_names.serialize_aws_json_1_0(
            value["metrics"]
        )
    if "granularity" in value:
        import capo_bcm_dashboards.types.granularity

        out["granularity"] = (
            capo_bcm_dashboards.types.granularity.serialize_aws_json_1_0(
                value["granularity"]
            )
        )
    if "group_by" in value:
        import capo_bcm_dashboards.types.group_definitions

        out["groupBy"] = (
            capo_bcm_dashboards.types.group_definitions.serialize_aws_json_1_0(
                value["group_by"]
            )
        )
    if "filter" in value:
        import capo_bcm_dashboards.types.expression

        out["filter"] = capo_bcm_dashboards.types.expression.serialize_aws_json_1_0(
            value["filter"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SavingsPlansCoverageQuery:
    out: SavingsPlansCoverageQuery = {}  # type: ignore[typeddict-item]
    if "timeRange" in data:
        import capo_bcm_dashboards.types.date_time_range

        out["time_range"] = (
            capo_bcm_dashboards.types.date_time_range.deserialize_aws_json_1_0(
                data["timeRange"]
            )
        )
    else:
        raise DeserializationError("SavingsPlansCoverageQuery.time_range required")
    if "metrics" in data:
        import capo_bcm_dashboards.types.metric_names

        out["metrics"] = (
            capo_bcm_dashboards.types.metric_names.deserialize_aws_json_1_0(
                data["metrics"]
            )
        )
    if "granularity" in data:
        import capo_bcm_dashboards.types.granularity

        out["granularity"] = (
            capo_bcm_dashboards.types.granularity.deserialize_aws_json_1_0(
                data["granularity"]
            )
        )
    if "groupBy" in data:
        import capo_bcm_dashboards.types.group_definitions

        out["group_by"] = (
            capo_bcm_dashboards.types.group_definitions.deserialize_aws_json_1_0(
                data["groupBy"]
            )
        )
    if "filter" in data:
        import capo_bcm_dashboards.types.expression

        out["filter"] = capo_bcm_dashboards.types.expression.deserialize_aws_json_1_0(
            data["filter"]
        )
    return out
