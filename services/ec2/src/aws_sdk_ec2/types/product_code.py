"""Generated from Smithy shape ``com.amazonaws.ec2#ProductCode``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.product_code_values
    import aws_sdk_ec2.types.string


class ProductCode(TypedDict):
    product_code_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The product code.</p>"""
    product_code_type: NotRequired[
        "aws_sdk_ec2.types.product_code_values.ProductCodeValues"
    ]
    """<p>The type of product code.</p>"""
