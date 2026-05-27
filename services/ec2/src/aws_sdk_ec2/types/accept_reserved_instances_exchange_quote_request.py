"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptReservedInstancesExchangeQuoteRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.reserved_instance_id_set
    import aws_sdk_ec2.types.target_configuration_request_set


class AcceptReservedInstancesExchangeQuoteRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    reserved_instance_ids: NotRequired[
        "aws_sdk_ec2.types.reserved_instance_id_set.ReservedInstanceIdSet"
    ]
    """<p>The IDs of the Convertible Reserved Instances to exchange for another Convertible Reserved Instance of the same or higher value.</p>"""
    target_configurations: NotRequired[
        "aws_sdk_ec2.types.target_configuration_request_set.TargetConfigurationRequestSet"
    ]
    """<p>The configuration of the target Convertible Reserved Instance to exchange for your current Convertible Reserved Instances.</p>"""
