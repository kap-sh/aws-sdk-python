"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMarketOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.market_type
    import aws_sdk_ec2.types.spot_market_options


class InstanceMarketOptionsRequest(TypedDict):
    market_type: NotRequired["aws_sdk_ec2.types.market_type.MarketType"]
    """<p>The market type.</p>"""
    spot_options: NotRequired["aws_sdk_ec2.types.spot_market_options.SpotMarketOptions"]
    """<p>The options for Spot Instances.</p>"""
