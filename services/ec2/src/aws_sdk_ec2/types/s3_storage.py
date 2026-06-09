"""Generated from Smithy shape ``com.amazonaws.ec2#S3Storage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: S3Storage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "aws_access_key_id" in value:
        pairs.append((f"{prefix}.AWSAccessKeyId", str(value["aws_access_key_id"])))
    if "bucket" in value:
        pairs.append((f"{prefix}.Bucket", str(value["bucket"])))
    if "prefix" in value:
        pairs.append((f"{prefix}.Prefix", str(value["prefix"])))
    if "upload_policy" in value:
        import aws_sdk_ec2.types.blob

        aws_sdk_ec2.types.blob.serialize_ec2_query(
            value["upload_policy"], pairs, f"{prefix}.UploadPolicy"
        )
    if "upload_policy_signature" in value:
        pairs.append(
            (f"{prefix}.UploadPolicySignature", str(value["upload_policy_signature"]))
        )


def deserialize_ec2_query(el: Element) -> S3Storage:
    out: S3Storage = {}  # type: ignore[typeddict-item]
    child_aws_access_key_id = el.find("AWSAccessKeyId")
    if child_aws_access_key_id is not None:
        out["aws_access_key_id"] = str(child_aws_access_key_id.text or "")
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_upload_policy = el.find("UploadPolicy")
    if child_upload_policy is not None:
        import aws_sdk_ec2.types.blob

        out["upload_policy"] = aws_sdk_ec2.types.blob.deserialize_ec2_query(
            child_upload_policy
        )
    child_upload_policy_signature = el.find("UploadPolicySignature")
    if child_upload_policy_signature is not None:
        out["upload_policy_signature"] = str(child_upload_policy_signature.text or "")
    return out
