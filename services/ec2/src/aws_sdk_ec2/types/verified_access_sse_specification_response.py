"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessSseSpecificationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.kms_key_arn


class VerifiedAccessSseSpecificationResponse(TypedDict):
    customer_managed_key_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether customer managed KMS keys are in use for server side encryption.</p> <p>Valid values: <code>True</code> | <code>False</code> </p>"""
    kms_key_arn: NotRequired["aws_sdk_ec2.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key.</p>"""
