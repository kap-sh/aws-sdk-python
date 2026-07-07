"""Generated from Smithy shape ``com.amazonaws.ec2#AssociatedRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string


class AssociatedRole(TypedDict, closed=True):
    associated_role_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the associated IAM role.</p>"""
    certificate_s3_bucket_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket in which the Amazon S3 object is stored.</p>"""
    certificate_s3_object_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The key of the Amazon S3 object where the certificate, certificate chain, and encrypted private key bundle are stored. The object key is formatted as follows: <code>role_arn</code>/<code>certificate_arn</code>. </p>"""
    encryption_kms_key_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the private key.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociatedRole, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "associated_role_arn" in value:
        pairs.append((f"{prefix}.AssociatedRoleArn", str(value["associated_role_arn"])))
    if "certificate_s3_bucket_name" in value:
        pairs.append(
            (
                f"{prefix}.CertificateS3BucketName",
                str(value["certificate_s3_bucket_name"]),
            )
        )
    if "certificate_s3_object_key" in value:
        pairs.append(
            (
                f"{prefix}.CertificateS3ObjectKey",
                str(value["certificate_s3_object_key"]),
            )
        )
    if "encryption_kms_key_id" in value:
        pairs.append(
            (f"{prefix}.EncryptionKmsKeyId", str(value["encryption_kms_key_id"]))
        )


def deserialize_ec2_query(el: Element) -> AssociatedRole:
    out: AssociatedRole = {}  # type: ignore[typeddict-item]
    child_associated_role_arn = el.find("AssociatedRoleArn")
    if child_associated_role_arn is not None:
        out["associated_role_arn"] = str(child_associated_role_arn.text or "")
    child_certificate_s3_bucket_name = el.find("CertificateS3BucketName")
    if child_certificate_s3_bucket_name is not None:
        out["certificate_s3_bucket_name"] = str(
            child_certificate_s3_bucket_name.text or ""
        )
    child_certificate_s3_object_key = el.find("CertificateS3ObjectKey")
    if child_certificate_s3_object_key is not None:
        out["certificate_s3_object_key"] = str(
            child_certificate_s3_object_key.text or ""
        )
    child_encryption_kms_key_id = el.find("EncryptionKmsKeyId")
    if child_encryption_kms_key_id is not None:
        out["encryption_kms_key_id"] = str(child_encryption_kms_key_id.text or "")
    return out
