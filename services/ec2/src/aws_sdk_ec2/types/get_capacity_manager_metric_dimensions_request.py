"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMetricDimensionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_manager_condition_set
    import aws_sdk_ec2.types.group_by_set
    import aws_sdk_ec2.types.max_results
    import aws_sdk_ec2.types.metric_set
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.next_token


class GetCapacityManagerMetricDimensionsRequest(TypedDict):
    group_by: NotRequired["aws_sdk_ec2.types.group_by_set.GroupBySet"]
    """<p> The dimensions to group by when retrieving available dimension values. This determines which dimension combinations are returned. Required parameter. </p>"""
    filter_by: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_condition_set.CapacityManagerConditionSet"
    ]
    """<p> Conditions to filter which dimension values are returned. Each filter specifies a dimension, comparison operator, and values to match against. </p>"""
    start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The start time for the dimension query, in ISO 8601 format. Only dimensions with data in this time range will be returned. </p>"""
    end_time: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p> The end time for the dimension query, in ISO 8601 format. Only dimensions with data in this time range will be returned. </p>"""
    metric_names: NotRequired["aws_sdk_ec2.types.metric_set.MetricSet"]
    """<p> The metric names to use as an additional filter when retrieving dimensions. Only dimensions that have data for these metrics will be returned. Required parameter with maximum size of 1 for v1. </p>"""
    max_results: NotRequired["aws_sdk_ec2.types.max_results.MaxResults"]
    """<p> The maximum number of dimension combinations to return. Valid range is 1 to 1000. Use with NextToken for pagination. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p> The token for the next page of results. Use this value in a subsequent call to retrieve additional dimension values. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetCapacityManagerMetricDimensionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "group_by" in value:
        import aws_sdk_ec2.types.group_by_set

        aws_sdk_ec2.types.group_by_set.serialize_ec2_query(
            value["group_by"], pairs, f"{prefix}.GroupBy"
        )
    if "filter_by" in value:
        import aws_sdk_ec2.types.capacity_manager_condition_set

        aws_sdk_ec2.types.capacity_manager_condition_set.serialize_ec2_query(
            value["filter_by"], pairs, f"{prefix}.FilterBy"
        )
    if "start_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )
    if "metric_names" in value:
        import aws_sdk_ec2.types.metric_set

        aws_sdk_ec2.types.metric_set.serialize_ec2_query(
            value["metric_names"], pairs, f"{prefix}.MetricNames"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> GetCapacityManagerMetricDimensionsRequest:
    out: GetCapacityManagerMetricDimensionsRequest = {}  # type: ignore[typeddict-item]
    if el.find("GroupBy") is not None:
        import aws_sdk_ec2.types.group_by_set

        out["group_by"] = aws_sdk_ec2.types.group_by_set.deserialize_ec2_query(
            el, "GroupBy"
        )
    if el.find("FilterBy") is not None:
        import aws_sdk_ec2.types.capacity_manager_condition_set

        out["filter_by"] = (
            aws_sdk_ec2.types.capacity_manager_condition_set.deserialize_ec2_query(
                el, "FilterBy"
            )
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["start_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_start_time
            )
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["end_time"] = aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_end_time
        )
    if el.find("MetricNames") is not None:
        import aws_sdk_ec2.types.metric_set

        out["metric_names"] = aws_sdk_ec2.types.metric_set.deserialize_ec2_query(
            el, "MetricNames"
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
