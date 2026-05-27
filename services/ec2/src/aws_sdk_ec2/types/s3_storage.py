"""Generated from Smithy shape ``com.amazonaws.ec2#S3Storage``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.blob
    import aws_sdk_ec2.types.s3_storage_upload_policy_signature
    import aws_sdk_ec2.types.string


class S3Storage(TypedDict):
    aws_access_key_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The access key ID of the owner of the bucket. Before you specify a value for your access key ID, review and follow the guidance in <a href=\"https://docs.aws.amazon.com/accounts/latest/reference/best-practices.html\">Best Practices for Amazon Web Services accounts</a> in the <i>Account ManagementReference Guide</i>.</p>"""
    bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The bucket in which to store the AMI. You can specify a bucket that you already own or a new bucket that Amazon EC2 creates on your behalf. If you specify a bucket that belongs to someone else, Amazon EC2 returns an error.</p>"""
    prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The beginning of the file name of the AMI.</p>"""
    upload_policy: NotRequired["aws_sdk_ec2.types.blob.Blob"]
    """<p>An Amazon S3 upload policy that gives Amazon EC2 permission to upload items into Amazon S3 on your behalf.</p>"""
    upload_policy_signature: NotRequired[
        "aws_sdk_ec2.types.s3_storage_upload_policy_signature.S3StorageUploadPolicySignature"
    ]
    """<p>The signature of the JSON document.</p>"""
