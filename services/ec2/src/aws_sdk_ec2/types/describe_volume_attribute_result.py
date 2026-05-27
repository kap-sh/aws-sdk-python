"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumeAttributeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attribute_boolean_value
    import aws_sdk_ec2.types.product_code_list
    import aws_sdk_ec2.types.string


class DescribeVolumeAttributeResult(TypedDict):
    auto_enable_io: NotRequired[
        "aws_sdk_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>The state of <code>autoEnableIO</code> attribute.</p>"""
    product_codes: NotRequired["aws_sdk_ec2.types.product_code_list.ProductCodeList"]
    """<p>A list of product codes.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the volume.</p>"""
