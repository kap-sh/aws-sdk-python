"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControl``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_encryption_control_exclusions
    import aws_sdk_ec2.types.vpc_encryption_control_id
    import aws_sdk_ec2.types.vpc_encryption_control_mode
    import aws_sdk_ec2.types.vpc_encryption_control_state
    import aws_sdk_ec2.types.vpc_id


class VpcEncryptionControl(TypedDict):
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC associated with the encryption control configuration.</p>"""
    vpc_encryption_control_id: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_id.VpcEncryptionControlId"
    ]
    """<p>The ID of the VPC Encryption Control configuration.</p>"""
    mode: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_mode.VpcEncryptionControlMode"
    ]
    """<p>The encryption mode for the VPC Encryption Control configuration.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_state.VpcEncryptionControlState"
    ]
    """<p>The current state of the VPC Encryption Control configuration.</p>"""
    state_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message providing additional information about the encryption control state.</p>"""
    resource_exclusions: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusions.VpcEncryptionControlExclusions"
    ]
    """<p>Information about resource exclusions for the VPC Encryption Control configuration.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the VPC Encryption Control configuration.</p>"""
