"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyEbsDefaultKmsKeyIdResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ModifyEbsDefaultKmsKeyIdResult(TypedDict):
    kms_key_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the default KMS key for encryption by default.</p>"""
