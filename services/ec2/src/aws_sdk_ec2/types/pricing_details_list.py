"""Generated from Smithy shape ``com.amazonaws.ec2#PricingDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.pricing_detail

PricingDetailsList: TypeAlias = list["aws_sdk_ec2.types.pricing_detail.PricingDetail"]
