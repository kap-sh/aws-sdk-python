"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input
    import aws_sdk_ec2.types.vpc_encryption_control_mode


class VpcEncryptionControlConfiguration(TypedDict):
    mode: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_mode.VpcEncryptionControlMode"
    ]
    """<p>The encryption mode for the VPC Encryption Control configuration.</p>"""
    internet_gateway_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude internet gateway traffic from encryption enforcement.</p>"""
    egress_only_internet_gateway_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude egress-only internet gateway traffic from encryption enforcement.</p>"""
    nat_gateway_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude NAT gateway traffic from encryption enforcement.</p>"""
    virtual_private_gateway_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude virtual private gateway traffic from encryption enforcement.</p>"""
    vpc_peering_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude VPC peering connection traffic from encryption enforcement.</p>"""
    lambda_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude Lambda function traffic from encryption enforcement.</p>"""
    vpc_lattice_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude VPC Lattice traffic from encryption enforcement.</p>"""
    elastic_file_system_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude Elastic File System traffic from encryption enforcement.</p>"""
