"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardExportOutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.s3_uri


class ModelCardExportOutputConfig(TypedDict):
    s3_output_path: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 output path to export your model card PDF.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardExportOutputConfig) -> dict:
    out: dict = {}
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelCardExportOutputConfig:
    out: ModelCardExportOutputConfig = {}  # type: ignore[typeddict-item]
    if "S3OutputPath" in data:
        out["s3_output_path"] = data["S3OutputPath"]
    return out
