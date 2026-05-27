"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetHistoryResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.fleet_id
    import aws_sdk_ec2.types.history_record_set
    import aws_sdk_ec2.types.string


class DescribeFleetHistoryResult(TypedDict):
    history_records: NotRequired[
        "aws_sdk_ec2.types.history_record_set.HistoryRecordSet"
    ]
    """<p>Information about the events in the history of the EC2 Fleet.</p>"""
    last_evaluated_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The last date and time for the events, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). All records up to this time were retrieved.</p> <p>If <code>nextToken</code> indicates that there are more items, this value is not present.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    fleet_id: NotRequired["aws_sdk_ec2.types.fleet_id.FleetId"]
    """<p>The ID of the EC Fleet.</p>"""
    start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The start date and time for the events, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
