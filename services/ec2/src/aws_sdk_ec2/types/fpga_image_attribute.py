"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaImageAttribute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.load_permission_list
    import aws_sdk_ec2.types.product_code_list
    import aws_sdk_ec2.types.string


class FpgaImageAttribute(TypedDict):
    fpga_image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the AFI.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the AFI.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the AFI.</p>"""
    load_permissions: NotRequired[
        "aws_sdk_ec2.types.load_permission_list.LoadPermissionList"
    ]
    """<p>The load permissions.</p>"""
    product_codes: NotRequired["aws_sdk_ec2.types.product_code_list.ProductCodeList"]
    """<p>The product codes.</p>"""
