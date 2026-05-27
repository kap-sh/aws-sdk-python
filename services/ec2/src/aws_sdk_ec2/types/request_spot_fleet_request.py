"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotFleetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.spot_fleet_request_config_data


class RequestSpotFleetRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    spot_fleet_request_config: NotRequired[
        "aws_sdk_ec2.types.spot_fleet_request_config_data.SpotFleetRequestConfigData"
    ]
    """<p>The configuration for the Spot Fleet request.</p>"""
