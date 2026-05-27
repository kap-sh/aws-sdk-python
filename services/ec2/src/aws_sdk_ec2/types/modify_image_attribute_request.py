"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyImageAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attribute_value
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.launch_permission_modifications
    import aws_sdk_ec2.types.operation_type
    import aws_sdk_ec2.types.organization_arn_string_list
    import aws_sdk_ec2.types.organizational_unit_arn_string_list
    import aws_sdk_ec2.types.product_code_string_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.user_group_string_list
    import aws_sdk_ec2.types.user_id_string_list


class ModifyImageAttributeRequest(TypedDict):
    attribute: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the attribute to modify.</p> <p>Valid values: <code>description</code> | <code>imdsSupport</code> | <code>launchPermission</code> </p>"""
    description: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>A new description for the AMI.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    launch_permission: NotRequired[
        "aws_sdk_ec2.types.launch_permission_modifications.LaunchPermissionModifications"
    ]
    """<p>A new launch permission for the AMI.</p>"""
    operation_type: NotRequired["aws_sdk_ec2.types.operation_type.OperationType"]
    """<p>The operation type. This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    product_codes: NotRequired[
        "aws_sdk_ec2.types.product_code_string_list.ProductCodeStringList"
    ]
    """<p>Not supported.</p>"""
    user_groups: NotRequired[
        "aws_sdk_ec2.types.user_group_string_list.UserGroupStringList"
    ]
    """<p>The user groups. This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    user_ids: NotRequired["aws_sdk_ec2.types.user_id_string_list.UserIdStringList"]
    """<p>The Amazon Web Services account IDs. This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The value of the attribute being modified. This parameter can be used only when the <code>Attribute</code> parameter is <code>description</code> or <code>imdsSupport</code>.</p>"""
    organization_arns: NotRequired[
        "aws_sdk_ec2.types.organization_arn_string_list.OrganizationArnStringList"
    ]
    """<p>The Amazon Resource Name (ARN) of an organization. This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    organizational_unit_arns: NotRequired[
        "aws_sdk_ec2.types.organizational_unit_arn_string_list.OrganizationalUnitArnStringList"
    ]
    """<p>The Amazon Resource Name (ARN) of an organizational unit (OU). This parameter can be used only when the <code>Attribute</code> parameter is <code>launchPermission</code>.</p>"""
    imds_support: NotRequired["aws_sdk_ec2.types.attribute_value.AttributeValue"]
    """<p>Set to <code>v2.0</code> to indicate that IMDSv2 is specified in the AMI. Instances launched from this AMI will have <code>HttpTokens</code> automatically set to <code>required</code> so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, <code>HttpPutResponseHopLimit</code> is set to <code>2</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration\">Configure the AMI</a> in the <i>Amazon EC2 User Guide</i>.</p> <important> <p>Do not use this parameter unless your AMI software supports IMDSv2. After you set the value to <code>v2.0</code>, you can't undo it. The only way to “reset” your AMI is to create a new AMI from the underlying snapshot.</p> </important>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
