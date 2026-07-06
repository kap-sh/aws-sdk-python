"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIMlflowConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_mlflow_experiment_name
    import aws_sdk_sagemaker.types.ai_mlflow_resource_arn
    import aws_sdk_sagemaker.types.ai_mlflow_run_name


class AIMlflowConfig(TypedDict, closed=True):
    mlflow_resource_arn: NotRequired[
        "aws_sdk_sagemaker.types.ai_mlflow_resource_arn.AIMlflowResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the SageMaker managed MLflow resource.</p>"""
    mlflow_experiment_name: NotRequired[
        "aws_sdk_sagemaker.types.ai_mlflow_experiment_name.AIMlflowExperimentName"
    ]
    """<p>The MLflow experiment name used for tracking.</p>"""
    mlflow_run_name: NotRequired[
        "aws_sdk_sagemaker.types.ai_mlflow_run_name.AIMlflowRunName"
    ]
    """<p>The MLflow run name used for tracking.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIMlflowConfig) -> dict:
    out: dict = {}
    if "mlflow_resource_arn" in value:
        out["MlflowResourceArn"] = value["mlflow_resource_arn"]
    if "mlflow_experiment_name" in value:
        out["MlflowExperimentName"] = value["mlflow_experiment_name"]
    if "mlflow_run_name" in value:
        out["MlflowRunName"] = value["mlflow_run_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AIMlflowConfig:
    out: AIMlflowConfig = {}  # type: ignore[typeddict-item]
    if "MlflowResourceArn" in data:
        out["mlflow_resource_arn"] = data["MlflowResourceArn"]
    if "MlflowExperimentName" in data:
        out["mlflow_experiment_name"] = data["MlflowExperimentName"]
    if "MlflowRunName" in data:
        out["mlflow_run_name"] = data["MlflowRunName"]
    return out
