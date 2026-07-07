"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceSqlHaHistoryStatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_instance_sql_ha_states_request_max_results_integer
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.instance_id_string_list
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.next_token


class DescribeInstanceSqlHaHistoryStatesRequest(TypedDict, closed=True):
    instance_ids: NotRequired[
        "aws_sdk_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The IDs of the SQL Server High Availability instances to describe. If omitted, the API returns historical states for all SQL Server High Availability instances.</p>"""
    start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start data and time of the period for which to get the historical SQL Server High Availability states. If omitted, the API returns all available historical states.</p> <p>Timezone: UTC</p> <p>Format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    end_time: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The end data and time of the period for which to get historical SQL Server High Availability states. If omitted, the API returns historical states up to the current date and time.</p> <p>Timezone: UTC</p> <p>Format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_instance_sql_ha_states_request_max_results_integer.DescribeInstanceSqlHaStatesRequestMaxResultsInteger"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned <code>nextToken</code> value.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters to apply to the results. Supported filters include:</p> <ul> <li> <p> <code>tag:<key></code> - The tag key and value pair assigned to the instance. For example, to find all instances tagged with <code>Owner:TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The tag key assigned to the instance.</p> </li> <li> <p> <code>haStatus</code> - The SQL Server High Availability status of the SQL Server High Availability instance (<code>processing</code> | <code>active</code> | <code>standby</code> | <code>invalid</code>).</p> </li> <li> <p> <code>sqlServerLicenseUsage</code> - The license type for the SQL Server license (<code>full</code> | <code>waived</code>).</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceSqlHaHistoryStatesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_ids" in value:
        import aws_sdk_ec2.types.instance_id_string_list

        aws_sdk_ec2.types.instance_id_string_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{prefix}.InstanceIds"
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
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeInstanceSqlHaHistoryStatesRequest:
    out: DescribeInstanceSqlHaHistoryStatesRequest = {}  # type: ignore[typeddict-item]
    if el.find("InstanceIds") is not None:
        import aws_sdk_ec2.types.instance_id_string_list

        out["instance_ids"] = (
            aws_sdk_ec2.types.instance_id_string_list.deserialize_ec2_query(
                el, "InstanceIds"
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
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
