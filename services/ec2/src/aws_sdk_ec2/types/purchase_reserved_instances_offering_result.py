"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseReservedInstancesOfferingResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PurchaseReservedInstancesOfferingResult(TypedDict):
    reserved_instances_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IDs of the purchased Reserved Instances. If your purchase crosses into a discounted pricing tier, the final Reserved Instances IDs might change. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-reserved-instances-application.html#crossing-pricing-tiers\">Crossing pricing tiers</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
