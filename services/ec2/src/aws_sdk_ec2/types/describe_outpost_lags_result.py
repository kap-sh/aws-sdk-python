"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeOutpostLagsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.outpost_lag_set
    import aws_sdk_ec2.types.string


class DescribeOutpostLagsResult(TypedDict):
    outpost_lags: NotRequired["aws_sdk_ec2.types.outpost_lag_set.OutpostLagSet"]
    """<p>The Outpost LAGs.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
