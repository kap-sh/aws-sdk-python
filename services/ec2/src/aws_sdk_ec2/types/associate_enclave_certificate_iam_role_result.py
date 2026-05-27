"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateEnclaveCertificateIamRoleResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AssociateEnclaveCertificateIamRoleResult(TypedDict):
    certificate_s3_bucket_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket to which the certificate was uploaded.</p>"""
    certificate_s3_object_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon S3 object key where the certificate, certificate chain, and encrypted private key bundle are stored. The object key is formatted as follows: <code>role_arn</code>/<code>certificate_arn</code>.</p>"""
    encryption_kms_key_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the private key of the certificate.</p>"""
