"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMetricDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_manager_condition_set
    import capo_ec2.types.group_by_set
    import capo_ec2.types.max_results
    import capo_ec2.types.metric_set
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.next_token
    import capo_ec2.types.period


class GetCapacityManagerMetricDataRequest(TypedDict, closed=True):
    metric_names: NotRequired["capo_ec2.types.metric_set.MetricSet"]
    """<p> The names of the metrics to retrieve. Maximum of 10 metrics per request. </p>"""
    start_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p> The start time for the metric data query, in ISO 8601 format. The time range (end time - start time) must be a multiple of the specified period. </p>"""
    end_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p> The end time for the metric data query, in ISO 8601 format. If the end time is beyond the latest ingested data, it will be automatically adjusted to the latest available data point. </p>"""
    period: NotRequired["capo_ec2.types.period.Period"]
    """<p> The granularity, in seconds, of the returned data points. </p>"""
    group_by: NotRequired["capo_ec2.types.group_by_set.GroupBySet"]
    """<p> The dimensions by which to group the metric data. This determines how the data is aggregated and returned. </p>"""
    filter_by: NotRequired[
        "capo_ec2.types.capacity_manager_condition_set.CapacityManagerConditionSet"
    ]
    """<p> Conditions to filter the metric data. Each filter specifies a dimension, comparison operator ('equals', 'in'), and values to match against. </p>"""
    max_results: NotRequired["capo_ec2.types.max_results.MaxResults"]
    """<p> The maximum number of data points to return. Valid range is 1 to 100,000. Use with NextToken for pagination of large result sets. </p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p> The token for the next page of results. Use this value in a subsequent call to retrieve additional data points. </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetCapacityManagerMetricDataRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "metric_names" in value:
        import capo_ec2.types.metric_set

        capo_ec2.types.metric_set.serialize_ec2_query(
            value["metric_names"], pairs, f"{prefix}.MetricNames"
        )
    if "start_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )
    if "period" in value:
        pairs.append((f"{prefix}.Period", str(value["period"])))
    if "group_by" in value:
        import capo_ec2.types.group_by_set

        capo_ec2.types.group_by_set.serialize_ec2_query(
            value["group_by"], pairs, f"{prefix}.GroupBy"
        )
    if "filter_by" in value:
        import capo_ec2.types.capacity_manager_condition_set

        capo_ec2.types.capacity_manager_condition_set.serialize_ec2_query(
            value["filter_by"], pairs, f"{prefix}.FilterBy"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> GetCapacityManagerMetricDataRequest:
    out: GetCapacityManagerMetricDataRequest = {}  # type: ignore[typeddict-item]
    if el.find("MetricNames") is not None:
        import capo_ec2.types.metric_set

        out["metric_names"] = capo_ec2.types.metric_set.deserialize_ec2_query(
            el, "MetricNames"
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["end_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_end_time
        )
    child_period = el.find("Period")
    if child_period is not None:
        out["period"] = int(child_period.text or "")
    if el.find("GroupBy") is not None:
        import capo_ec2.types.group_by_set

        out["group_by"] = capo_ec2.types.group_by_set.deserialize_ec2_query(
            el, "GroupBy"
        )
    if el.find("FilterBy") is not None:
        import capo_ec2.types.capacity_manager_condition_set

        out["filter_by"] = (
            capo_ec2.types.capacity_manager_condition_set.deserialize_ec2_query(
                el, "FilterBy"
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
