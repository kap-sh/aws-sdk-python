"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceMarketOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_spot_market_options
    import aws_sdk_ec2.types.market_type


class LaunchTemplateInstanceMarketOptions(TypedDict):
    market_type: NotRequired["aws_sdk_ec2.types.market_type.MarketType"]
    """<p>The market type.</p>"""
    spot_options: NotRequired[
        "aws_sdk_ec2.types.launch_template_spot_market_options.LaunchTemplateSpotMarketOptions"
    ]
    """<p>The options for Spot Instances.</p>"""
