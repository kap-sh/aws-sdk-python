"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerCondition``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dimension_condition


class CapacityManagerCondition(TypedDict):
    dimension_condition: NotRequired[
        "aws_sdk_ec2.types.dimension_condition.DimensionCondition"
    ]
    """<p> The dimension-based condition that specifies how to filter the data based on dimension values. </p>"""
