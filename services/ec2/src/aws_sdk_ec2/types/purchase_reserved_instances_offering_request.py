"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseReservedInstancesOfferingRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.reserved_instance_limit_price
    import aws_sdk_ec2.types.reserved_instances_offering_id


class PurchaseReservedInstancesOfferingRequest(TypedDict):
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of Reserved Instances to purchase.</p>"""
    reserved_instances_offering_id: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_offering_id.ReservedInstancesOfferingId"
    ]
    """<p>The ID of the Reserved Instance offering to purchase.</p>"""
    purchase_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time at which to purchase the Reserved Instance, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    limit_price: NotRequired[
        "aws_sdk_ec2.types.reserved_instance_limit_price.ReservedInstanceLimitPrice"
    ]
    """<p>Specified for Reserved Instance Marketplace offerings to limit the total order and ensure that the Reserved Instances are not purchased at unexpected prices.</p>"""
