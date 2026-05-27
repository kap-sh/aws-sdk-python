"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotPriceHistoryResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_price_history_list
    import aws_sdk_ec2.types.string


class DescribeSpotPriceHistoryResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is an empty string (<code>\"\"</code>) or <code>null</code> when there are no more items to return.</p>"""
    spot_price_history: NotRequired[
        "aws_sdk_ec2.types.spot_price_history_list.SpotPriceHistoryList"
    ]
    """<p>The historical Spot prices.</p>"""
