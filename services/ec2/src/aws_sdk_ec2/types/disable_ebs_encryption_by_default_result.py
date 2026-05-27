"""Generated from Smithy shape ``com.amazonaws.ec2#DisableEbsEncryptionByDefaultResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class DisableEbsEncryptionByDefaultResult(TypedDict):
    ebs_encryption_by_default: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The updated status of encryption by default.</p>"""
