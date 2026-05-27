"""Generated from Smithy shape ``com.amazonaws.ec2#TargetConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.reserved_instances_offering_id


class TargetConfigurationRequest(TypedDict):
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances the Convertible Reserved Instance offering can be applied to. This parameter is reserved and cannot be specified in a request</p>"""
    offering_id: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_offering_id.ReservedInstancesOfferingId"
    ]
    """<p>The Convertible Reserved Instance offering ID.</p>"""
