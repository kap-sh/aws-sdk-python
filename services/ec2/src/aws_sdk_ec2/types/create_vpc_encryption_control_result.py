"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEncryptionControlResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_encryption_control


class CreateVpcEncryptionControlResult(TypedDict):
    vpc_encryption_control: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control.VpcEncryptionControl"
    ]
    """<p>Information about the VPC Encryption Control configuration.</p>"""
