"""Generated from Smithy shape ``com.amazonaws.sagemaker#SharingSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.kms_key_id
    import aws_sdk_sagemaker.types.notebook_output_option
    import aws_sdk_sagemaker.types.s3_uri


class SharingSettings(TypedDict):
    notebook_output_option: NotRequired[
        "aws_sdk_sagemaker.types.notebook_output_option.NotebookOutputOption"
    ]
    """<p>Whether to include the notebook cell output when sharing the notebook. The default is <code>Disabled</code>.</p>"""
    s3_output_path: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>When <code>NotebookOutputOption</code> is <code>Allowed</code>, the Amazon S3 bucket used to store the shared notebook snapshots.</p>"""
    s3_kms_key_id: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>When <code>NotebookOutputOption</code> is <code>Allowed</code>, the Amazon Web Services Key Management Service (KMS) encryption key ID used to encrypt the notebook cell output in the Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharingSettings) -> dict:
    out: dict = {}
    if "notebook_output_option" in value:
        import aws_sdk_sagemaker.types.notebook_output_option

        out["NotebookOutputOption"] = (
            aws_sdk_sagemaker.types.notebook_output_option.serialize_aws_json_1_1(
                value["notebook_output_option"]
            )
        )
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    if "s3_kms_key_id" in value:
        out["S3KmsKeyId"] = value["s3_kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SharingSettings:
    out: SharingSettings = {}  # type: ignore[typeddict-item]
    if "NotebookOutputOption" in data:
        import aws_sdk_sagemaker.types.notebook_output_option

        out["notebook_output_option"] = (
            aws_sdk_sagemaker.types.notebook_output_option.deserialize_aws_json_1_1(
                data["NotebookOutputOption"]
            )
        )
    if "S3OutputPath" in data:
        out["s3_output_path"] = data["S3OutputPath"]
    if "S3KmsKeyId" in data:
        out["s3_kms_key_id"] = data["S3KmsKeyId"]
    return out
