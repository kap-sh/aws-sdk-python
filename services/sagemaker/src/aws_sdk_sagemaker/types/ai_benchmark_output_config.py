"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIBenchmarkOutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_mlflow_config
    import aws_sdk_sagemaker.types.s3_uri


class AIBenchmarkOutputConfig(TypedDict):
    s3_output_location: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 URI where benchmark results are stored.</p>"""
    mlflow_config: NotRequired[
        "aws_sdk_sagemaker.types.ai_mlflow_config.AIMlflowConfig"
    ]
    """<p>The MLflow tracking configuration for the job. If you don't specify this parameter, MLflow tracking is disabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIBenchmarkOutputConfig) -> dict:
    out: dict = {}
    if "s3_output_location" in value:
        out["S3OutputLocation"] = value["s3_output_location"]
    if "mlflow_config" in value:
        import aws_sdk_sagemaker.types.ai_mlflow_config

        out["MlflowConfig"] = (
            aws_sdk_sagemaker.types.ai_mlflow_config.serialize_aws_json_1_1(
                value["mlflow_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIBenchmarkOutputConfig:
    out: AIBenchmarkOutputConfig = {}  # type: ignore[typeddict-item]
    if "S3OutputLocation" in data:
        out["s3_output_location"] = data["S3OutputLocation"]
    if "MlflowConfig" in data:
        import aws_sdk_sagemaker.types.ai_mlflow_config

        out["mlflow_config"] = (
            aws_sdk_sagemaker.types.ai_mlflow_config.deserialize_aws_json_1_1(
                data["MlflowConfig"]
            )
        )
    return out
