"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpcEncryptionControlResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_encryption_control


class DeleteVpcEncryptionControlResult(TypedDict):
    vpc_encryption_control: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control.VpcEncryptionControl"
    ]
    """<p>Information about the deleted VPC Encryption Control configuration.</p>"""
