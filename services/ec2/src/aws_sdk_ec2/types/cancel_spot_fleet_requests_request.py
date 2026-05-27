"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.spot_fleet_request_id_list


class CancelSpotFleetRequestsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    spot_fleet_request_ids: NotRequired[
        "aws_sdk_ec2.types.spot_fleet_request_id_list.SpotFleetRequestIdList"
    ]
    """<p>The IDs of the Spot Fleet requests.</p> <p>Constraint: You can specify up to 100 IDs in a single request.</p>"""
    terminate_instances: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to terminate the associated instances when the Spot Fleet request is canceled. The default is to terminate the instances.</p> <p>To let the instances continue to run after the Spot Fleet request is canceled, specify <code>no-terminate-instances</code>.</p>"""
