"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceSqlHaHistoryStatesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_instance_sql_ha_states_request_max_results_integer
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.instance_id_string_list
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.next_token


class DescribeInstanceSqlHaHistoryStatesRequest(TypedDict):
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
