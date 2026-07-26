"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateEnclaveCertificateIamRoleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class AssociateEnclaveCertificateIamRoleResult(TypedDict, closed=True):
    certificate_s3_bucket_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket to which the certificate was uploaded.</p>"""
    certificate_s3_object_key: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon S3 object key where the certificate, certificate chain, and encrypted private key bundle are stored. The object key is formatted as follows: <code>role_arn</code>/<code>certificate_arn</code>.</p>"""
    encryption_kms_key_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the private key of the certificate.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateEnclaveCertificateIamRoleResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
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


def deserialize_ec2_query(el: Element) -> AssociateEnclaveCertificateIamRoleResult:
    out: AssociateEnclaveCertificateIamRoleResult = {}  # type: ignore[typeddict-item]
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
