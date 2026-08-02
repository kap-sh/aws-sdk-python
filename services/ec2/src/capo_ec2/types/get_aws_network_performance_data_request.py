"""Generated from Smithy shape ``com.amazonaws.ec2#GetAwsNetworkPerformanceDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.data_queries
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class GetAwsNetworkPerformanceDataRequest(TypedDict, closed=True):
    data_queries: NotRequired["capo_ec2.types.data_queries.DataQueries"]
    """<p>A list of network performance data queries.</p>"""
    start_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The starting time for the performance data request. The starting time must be formatted as <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2022-06-10T12:00:00.000Z</code>.</p>"""
    end_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The ending time for the performance data request. The end time must be formatted as <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2022-06-12T12:00:00.000Z</code>.</p>"""
    max_results: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetAwsNetworkPerformanceDataRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "data_queries" in value:
        import capo_ec2.types.data_queries

        capo_ec2.types.data_queries.serialize_ec2_query(
            value["data_queries"], pairs, f"{key_prefix}DataQueries"
        )
    if "start_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "end_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_time"], pairs, f"{key_prefix}EndTime"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> GetAwsNetworkPerformanceDataRequest:
    out: GetAwsNetworkPerformanceDataRequest = {}  # type: ignore[typeddict-item]
    if el.find("DataQueries") is not None:
        import capo_ec2.types.data_queries

        out["data_queries"] = capo_ec2.types.data_queries.deserialize_ec2_query(
            el, "DataQueries"
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
