"""Generated from Smithy shape ``com.amazonaws.ssoadmin#EncryptionConfigurationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.kms_key_arn
    import aws_sdk_sso_admin.types.kms_key_status
    import aws_sdk_sso_admin.types.kms_key_type
    import aws_sdk_sso_admin.types.reason


class EncryptionConfigurationDetails(TypedDict):
    key_type: NotRequired["aws_sdk_sso_admin.types.kms_key_type.KmsKeyType"]
    """<p>The type of KMS key used for encryption.</p>"""
    kms_key_arn: NotRequired["aws_sdk_sso_admin.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key currently used to encrypt data in your IAM Identity Center instance. </p>"""
    encryption_status: NotRequired[
        "aws_sdk_sso_admin.types.kms_key_status.KmsKeyStatus"
    ]
    """<p>The current status of encryption configuration.</p>"""
    encryption_status_reason: NotRequired["aws_sdk_sso_admin.types.reason.Reason"]
    """<p>Provides additional context about the current encryption status. This field is particularly useful when the encryption status is UPDATE_FAILED. When encryption configuration update fails, this field contains information about the cause, which may include KMS key access issues, key not found errors, invalid key configuration, key in an invalid state, or a disabled key. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionConfigurationDetails) -> dict:
    out: dict = {}
    if "key_type" in value:
        import aws_sdk_sso_admin.types.kms_key_type

        out["KeyType"] = aws_sdk_sso_admin.types.kms_key_type.serialize_aws_json_1_1(
            value["key_type"]
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "encryption_status" in value:
        import aws_sdk_sso_admin.types.kms_key_status

        out["EncryptionStatus"] = (
            aws_sdk_sso_admin.types.kms_key_status.serialize_aws_json_1_1(
                value["encryption_status"]
            )
        )
    if "encryption_status_reason" in value:
        out["EncryptionStatusReason"] = value["encryption_status_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionConfigurationDetails:
    out: EncryptionConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "KeyType" in data:
        import aws_sdk_sso_admin.types.kms_key_type

        out["key_type"] = aws_sdk_sso_admin.types.kms_key_type.deserialize_aws_json_1_1(
            data["KeyType"]
        )
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "EncryptionStatus" in data:
        import aws_sdk_sso_admin.types.kms_key_status

        out["encryption_status"] = (
            aws_sdk_sso_admin.types.kms_key_status.deserialize_aws_json_1_1(
                data["EncryptionStatus"]
            )
        )
    if "EncryptionStatusReason" in data:
        out["encryption_status_reason"] = data["EncryptionStatusReason"]
    return out
