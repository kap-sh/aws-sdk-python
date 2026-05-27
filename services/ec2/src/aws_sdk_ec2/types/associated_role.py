"""Generated from Smithy shape ``com.amazonaws.ec2#AssociatedRole``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string


class AssociatedRole(TypedDict):
    associated_role_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the associated IAM role.</p>"""
    certificate_s3_bucket_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket in which the Amazon S3 object is stored.</p>"""
    certificate_s3_object_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The key of the Amazon S3 object where the certificate, certificate chain, and encrypted private key bundle are stored. The object key is formatted as follows: <code>role_arn</code>/<code>certificate_arn</code>. </p>"""
    encryption_kms_key_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the private key.</p>"""
