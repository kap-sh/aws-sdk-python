"""Generated from Smithy shape ``com.amazonaws.ec2#MarketplaceProductCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.marketplace_product_code

MarketplaceProductCodeList: TypeAlias = list[
    "aws_sdk_ec2.types.marketplace_product_code.MarketplaceProductCode"
]
