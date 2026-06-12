"""Generated from Smithy shape ``com.amazonaws.glue#JobBookmarksEncryption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.job_bookmarks_encryption_mode
    import aws_sdk_glue.types.kms_key_arn


class JobBookmarksEncryption(TypedDict):
    job_bookmarks_encryption_mode: NotRequired[
        "aws_sdk_glue.types.job_bookmarks_encryption_mode.JobBookmarksEncryptionMode"
    ]
    """<p>The encryption mode to use for job bookmarks data.</p>"""
    kms_key_arn: NotRequired["aws_sdk_glue.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobBookmarksEncryption) -> dict:
    out: dict = {}
    if "job_bookmarks_encryption_mode" in value:
        import aws_sdk_glue.types.job_bookmarks_encryption_mode

        out["JobBookmarksEncryptionMode"] = (
            aws_sdk_glue.types.job_bookmarks_encryption_mode.serialize_aws_json_1_1(
                value["job_bookmarks_encryption_mode"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobBookmarksEncryption:
    out: JobBookmarksEncryption = {}  # type: ignore[typeddict-item]
    if "JobBookmarksEncryptionMode" in data:
        import aws_sdk_glue.types.job_bookmarks_encryption_mode

        out["job_bookmarks_encryption_mode"] = (
            aws_sdk_glue.types.job_bookmarks_encryption_mode.deserialize_aws_json_1_1(
                data["JobBookmarksEncryptionMode"]
            )
        )
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
