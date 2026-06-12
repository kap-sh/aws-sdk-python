"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEncryption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_encryption_mode
    import aws_sdk_glue.types.kms_key_arn


class DataQualityEncryption(TypedDict):
    data_quality_encryption_mode: NotRequired[
        "aws_sdk_glue.types.data_quality_encryption_mode.DataQualityEncryptionMode"
    ]
    """<p>The encryption mode to use for encrypting Data Quality assets. These assets include data quality rulesets, results, statistics, anomaly detection models and observations.</p> <p>Valid values are <code>SSEKMS</code> for encryption using a customer-managed KMS key, or <code>DISABLED</code>.</p>"""
    kms_key_arn: NotRequired["aws_sdk_glue.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEncryption) -> dict:
    out: dict = {}
    if "data_quality_encryption_mode" in value:
        import aws_sdk_glue.types.data_quality_encryption_mode

        out["DataQualityEncryptionMode"] = (
            aws_sdk_glue.types.data_quality_encryption_mode.serialize_aws_json_1_1(
                value["data_quality_encryption_mode"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityEncryption:
    out: DataQualityEncryption = {}  # type: ignore[typeddict-item]
    if "DataQualityEncryptionMode" in data:
        import aws_sdk_glue.types.data_quality_encryption_mode

        out["data_quality_encryption_mode"] = (
            aws_sdk_glue.types.data_quality_encryption_mode.deserialize_aws_json_1_1(
                data["DataQualityEncryptionMode"]
            )
        )
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
