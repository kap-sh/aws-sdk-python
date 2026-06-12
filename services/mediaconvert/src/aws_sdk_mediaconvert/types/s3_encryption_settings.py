"""Generated from Smithy shape ``com.amazonaws.mediaconvert#S3EncryptionSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string_pattern_a_za_z0902
    import aws_sdk_mediaconvert.types.__string_pattern_arn_aws_us_gov_cn_kms_az26_east_west_central_north_south_east_west1912_d12_key_afaf098_afaf094_afaf094_afaf094_afaf0912_mrk_afaf0932
    import aws_sdk_mediaconvert.types.s3_server_side_encryption_type


class S3EncryptionSettings(TypedDict):
    encryption_type: NotRequired[
        "aws_sdk_mediaconvert.types.s3_server_side_encryption_type.S3ServerSideEncryptionType"
    ]
    """Specify how you want your data keys managed. AWS uses data keys to encrypt your content. AWS also encrypts the data keys themselves, using a customer master key (CMK), and then stores the encrypted data keys alongside your encrypted content. Use this setting to specify which AWS service manages the CMK. For simplest set up, choose Amazon S3. If you want your master key to be managed by AWS Key Management Service (KMS), choose AWS KMS. By default, when you choose AWS KMS, KMS uses the AWS managed customer master key (CMK) associated with Amazon S3 to encrypt your data keys. You can optionally choose to specify a different, customer managed CMK. Do so by specifying the Amazon Resource Name (ARN) of the key for the setting KMS ARN."""
    kms_encryption_context: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_a_za_z0902.__stringPatternAZaZ0902"
    ]
    """Optionally, specify the encryption context that you want to use alongside your KMS key. AWS KMS uses this encryption context as additional authenticated data (AAD) to support authenticated encryption. This value must be a base64-encoded UTF-8 string holding JSON which represents a string-string map. To use this setting, you must also set Server-side encryption to AWS KMS. For more information about encryption context, see: https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context."""
    kms_key_arn: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_arn_aws_us_gov_cn_kms_az26_east_west_central_north_south_east_west1912_d12_key_afaf098_afaf094_afaf094_afaf094_afaf0912_mrk_afaf0932.__stringPatternArnAwsUsGovCnKmsAZ26EastWestCentralNorthSouthEastWest1912D12KeyAFAF098AFAF094AFAF094AFAF094AFAF0912MrkAFAF0932"
    ]
    """Optionally, specify the customer master key (CMK) that you want to use to encrypt the data key that AWS uses to encrypt your output content. Enter the Amazon Resource Name (ARN) of the CMK. To use this setting, you must also set Server-side encryption to AWS KMS. If you set Server-side encryption to AWS KMS but don't specify a CMK here, AWS uses the AWS managed CMK associated with Amazon S3."""


# --- restJson1 ser/de ---
def serialize_json(value: S3EncryptionSettings) -> dict:
    out: dict = {}
    if "encryption_type" in value:
        import aws_sdk_mediaconvert.types.s3_server_side_encryption_type

        out["encryptionType"] = (
            aws_sdk_mediaconvert.types.s3_server_side_encryption_type.serialize_json(
                value["encryption_type"]
            )
        )
    if "kms_encryption_context" in value:
        out["kmsEncryptionContext"] = value["kms_encryption_context"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> S3EncryptionSettings:
    out: S3EncryptionSettings = {}  # type: ignore[typeddict-item]
    if "encryptionType" in data:
        import aws_sdk_mediaconvert.types.s3_server_side_encryption_type

        out["encryption_type"] = (
            aws_sdk_mediaconvert.types.s3_server_side_encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    if "kmsEncryptionContext" in data:
        out["kms_encryption_context"] = data["kmsEncryptionContext"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
