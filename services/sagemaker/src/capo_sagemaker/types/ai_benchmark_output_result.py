"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIBenchmarkOutputResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_cloud_watch_logs_list
    import capo_sagemaker.types.ai_mlflow_config
    import capo_sagemaker.types.s3_uri


class AIBenchmarkOutputResult(TypedDict, closed=True):
    s3_output_location: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 URI where benchmark results are stored.</p>"""
    cloud_watch_logs: NotRequired[
        "capo_sagemaker.types.ai_cloud_watch_logs_list.AICloudWatchLogsList"
    ]
    """<p>The CloudWatch log information for the benchmark job.</p>"""
    mlflow_config: NotRequired["capo_sagemaker.types.ai_mlflow_config.AIMlflowConfig"]
    """<p>The MLflow tracking configuration for the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIBenchmarkOutputResult) -> dict:
    out: dict = {}
    if "s3_output_location" in value:
        out["S3OutputLocation"] = value["s3_output_location"]
    if "cloud_watch_logs" in value:
        import capo_sagemaker.types.ai_cloud_watch_logs_list

        out["CloudWatchLogs"] = (
            capo_sagemaker.types.ai_cloud_watch_logs_list.serialize_aws_json_1_1(
                value["cloud_watch_logs"]
            )
        )
    if "mlflow_config" in value:
        import capo_sagemaker.types.ai_mlflow_config

        out["MlflowConfig"] = (
            capo_sagemaker.types.ai_mlflow_config.serialize_aws_json_1_1(
                value["mlflow_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIBenchmarkOutputResult:
    out: AIBenchmarkOutputResult = {}  # type: ignore[typeddict-item]
    if "S3OutputLocation" in data:
        out["s3_output_location"] = data["S3OutputLocation"]
    if "CloudWatchLogs" in data:
        import capo_sagemaker.types.ai_cloud_watch_logs_list

        out["cloud_watch_logs"] = (
            capo_sagemaker.types.ai_cloud_watch_logs_list.deserialize_aws_json_1_1(
                data["CloudWatchLogs"]
            )
        )
    if "MlflowConfig" in data:
        import capo_sagemaker.types.ai_mlflow_config

        out["mlflow_config"] = (
            capo_sagemaker.types.ai_mlflow_config.deserialize_aws_json_1_1(
                data["MlflowConfig"]
            )
        )
    return out
