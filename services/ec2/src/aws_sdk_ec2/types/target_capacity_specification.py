"""Generated from Smithy shape ``com.amazonaws.ec2#TargetCapacitySpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.default_target_capacity_type
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.target_capacity_unit_type


class TargetCapacitySpecification(TypedDict):
    total_target_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of units to request, filled the default target capacity type.</p>"""
    on_demand_target_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of On-Demand units to request. If you specify a target capacity for Spot units, you cannot specify a target capacity for On-Demand units.</p>"""
    spot_target_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of Spot units to launch. If you specify a target capacity for On-Demand units, you cannot specify a target capacity for Spot units.</p>"""
    default_target_capacity_type: NotRequired[
        "aws_sdk_ec2.types.default_target_capacity_type.DefaultTargetCapacityType"
    ]
    """<p>The default target capacity type.</p>"""
    target_capacity_unit_type: NotRequired[
        "aws_sdk_ec2.types.target_capacity_unit_type.TargetCapacityUnitType"
    ]
    """<p>The unit for the target capacity.</p>"""
