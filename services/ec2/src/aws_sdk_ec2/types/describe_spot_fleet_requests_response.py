"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotFleetRequestsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_fleet_request_config_set
    import aws_sdk_ec2.types.string


class DescribeSpotFleetRequestsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    spot_fleet_request_configs: NotRequired[
        "aws_sdk_ec2.types.spot_fleet_request_config_set.SpotFleetRequestConfigSet"
    ]
    """<p>Information about the configuration of your Spot Fleet.</p>"""
