"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyFpgaImageAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.fpga_image_attribute_name
    import aws_sdk_ec2.types.fpga_image_id
    import aws_sdk_ec2.types.load_permission_modifications
    import aws_sdk_ec2.types.operation_type
    import aws_sdk_ec2.types.product_code_string_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.user_group_string_list
    import aws_sdk_ec2.types.user_id_string_list


class ModifyFpgaImageAttributeRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    fpga_image_id: NotRequired["aws_sdk_ec2.types.fpga_image_id.FpgaImageId"]
    """<p>The ID of the AFI.</p>"""
    attribute: NotRequired[
        "aws_sdk_ec2.types.fpga_image_attribute_name.FpgaImageAttributeName"
    ]
    """<p>The name of the attribute.</p>"""
    operation_type: NotRequired["aws_sdk_ec2.types.operation_type.OperationType"]
    """<p>The operation type.</p>"""
    user_ids: NotRequired["aws_sdk_ec2.types.user_id_string_list.UserIdStringList"]
    """<p>The Amazon Web Services account IDs. This parameter is valid only when modifying the <code>loadPermission</code> attribute.</p>"""
    user_groups: NotRequired[
        "aws_sdk_ec2.types.user_group_string_list.UserGroupStringList"
    ]
    """<p>The user groups. This parameter is valid only when modifying the <code>loadPermission</code> attribute.</p>"""
    product_codes: NotRequired[
        "aws_sdk_ec2.types.product_code_string_list.ProductCodeStringList"
    ]
    """<p>The product codes. After you add a product code to an AFI, it can't be removed. This parameter is valid only when modifying the <code>productCodes</code> attribute.</p>"""
    load_permission: NotRequired[
        "aws_sdk_ec2.types.load_permission_modifications.LoadPermissionModifications"
    ]
    """<p>The load permission for the AFI.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the AFI.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A name for the AFI.</p>"""
