"""Generated from Smithy shape ``com.amazonaws.ec2#SpotPriceHistoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_price

SpotPriceHistoryList: TypeAlias = list["aws_sdk_ec2.types.spot_price.SpotPrice"]
