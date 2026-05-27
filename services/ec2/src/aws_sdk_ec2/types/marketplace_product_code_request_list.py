"""Generated from Smithy shape ``com.amazonaws.ec2#MarketplaceProductCodeRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.marketplace_product_code_request

MarketplaceProductCodeRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.marketplace_product_code_request.MarketplaceProductCodeRequest"
]
