"""Generated from Smithy shape ``com.amazonaws.glue#CloudWatchEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.cloud_watch_encryption_mode
    import capo_glue.types.kms_key_arn


class CloudWatchEncryption(TypedDict, closed=True):
    cloud_watch_encryption_mode: NotRequired[
        "capo_glue.types.cloud_watch_encryption_mode.CloudWatchEncryptionMode"
    ]
    """<p>The encryption mode to use for CloudWatch data.</p>"""
    kms_key_arn: NotRequired["capo_glue.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchEncryption) -> dict:
    out: dict = {}
    if "cloud_watch_encryption_mode" in value:
        import capo_glue.types.cloud_watch_encryption_mode

        out["CloudWatchEncryptionMode"] = (
            capo_glue.types.cloud_watch_encryption_mode.serialize_aws_json_1_1(
                value["cloud_watch_encryption_mode"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchEncryption:
    out: CloudWatchEncryption = {}  # type: ignore[typeddict-item]
    if "CloudWatchEncryptionMode" in data:
        import capo_glue.types.cloud_watch_encryption_mode

        out["cloud_watch_encryption_mode"] = (
            capo_glue.types.cloud_watch_encryption_mode.deserialize_aws_json_1_1(
                data["CloudWatchEncryptionMode"]
            )
        )
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
