"""Generated from Smithy shape ``com.amazonaws.sagemaker#TensorBoardOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.directory_path
    import aws_sdk_sagemaker.types.s3_uri


class TensorBoardOutputConfig(TypedDict, closed=True):
    local_path: NotRequired["aws_sdk_sagemaker.types.directory_path.DirectoryPath"]
    """<p>Path to local storage location for tensorBoard output. Defaults to <code>/opt/ml/output/tensorboard</code>.</p>"""
    s3_output_path: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>Path to Amazon S3 storage location for TensorBoard output.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TensorBoardOutputConfig) -> dict:
    out: dict = {}
    if "local_path" in value:
        out["LocalPath"] = value["local_path"]
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TensorBoardOutputConfig:
    out: TensorBoardOutputConfig = {}  # type: ignore[typeddict-item]
    if "LocalPath" in data:
        out["local_path"] = data["LocalPath"]
    if "S3OutputPath" in data:
        out["s3_output_path"] = data["S3OutputPath"]
    return out
