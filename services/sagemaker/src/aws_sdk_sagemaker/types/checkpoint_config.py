"""Generated from Smithy shape ``com.amazonaws.sagemaker#CheckpointConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.directory_path
    import aws_sdk_sagemaker.types.s3_uri


class CheckpointConfig(TypedDict, closed=True):
    s3_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>Identifies the S3 path where you want SageMaker to store checkpoints. For example, <code>s3://bucket-name/key-name-prefix</code>.</p>"""
    local_path: NotRequired["aws_sdk_sagemaker.types.directory_path.DirectoryPath"]
    """<p>(Optional) The local directory where checkpoints are written. The default directory is <code>/opt/ml/checkpoints/</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckpointConfig) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "local_path" in value:
        out["LocalPath"] = value["local_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckpointConfig:
    out: CheckpointConfig = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    if "LocalPath" in data:
        out["local_path"] = data["LocalPath"]
    return out
