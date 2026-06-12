"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails(
    TypedDict
):
    encryption_option: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Indicates whether Amazon Simple Storage Service (Amazon S3) server-side encryption with Amazon S3 managed keys (SSE_S3), server-side encryption with KMS keys (SSE_KMS), or client-side encryption with KMS customer managed keys (CSE_KMS) is used. </p>"""
    kms_key: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> For <code>SSE_KMS</code> and <code>CSE_KMS</code>, this is the KMS key Amazon Resource Name (ARN) or ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails,
) -> dict:
    out: dict = {}
    if "encryption_option" in value:
        out["EncryptionOption"] = value["encryption_option"]
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    return out


def deserialize_json(
    data: dict,
) -> AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails:
    out: AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "EncryptionOption" in data:
        out["encryption_option"] = data["EncryptionOption"]
    if "KmsKey" in data:
        out["kms_key"] = data["KmsKey"]
    return out
