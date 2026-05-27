"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotFleetRequestHistoryResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.history_records
    import aws_sdk_ec2.types.string


class DescribeSpotFleetRequestHistoryResponse(TypedDict):
    history_records: NotRequired["aws_sdk_ec2.types.history_records.HistoryRecords"]
    """<p>Information about the events in the history of the Spot Fleet request.</p>"""
    last_evaluated_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The last date and time for the events, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). All records up to this time were retrieved.</p> <p>If <code>nextToken</code> indicates that there are more items, this value is not present.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    spot_fleet_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Spot Fleet request.</p>"""
    start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The starting date and time for the events, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
