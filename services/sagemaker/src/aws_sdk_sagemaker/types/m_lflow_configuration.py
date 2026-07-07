"""Generated from Smithy shape ``com.amazonaws.sagemaker#MLflowConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.m_lflow_arn
    import aws_sdk_sagemaker.types.mlflow_experiment_entity_name


class MLflowConfiguration(TypedDict, closed=True):
    mlflow_resource_arn: NotRequired["aws_sdk_sagemaker.types.m_lflow_arn.MLflowArn"]
    """<p> The Amazon Resource Name (ARN) of MLflow configuration resource. </p>"""
    mlflow_experiment_name: NotRequired[
        "aws_sdk_sagemaker.types.mlflow_experiment_entity_name.MlflowExperimentEntityName"
    ]
    """<p> The name of the MLflow configuration. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MLflowConfiguration) -> dict:
    out: dict = {}
    if "mlflow_resource_arn" in value:
        out["MlflowResourceArn"] = value["mlflow_resource_arn"]
    if "mlflow_experiment_name" in value:
        out["MlflowExperimentName"] = value["mlflow_experiment_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MLflowConfiguration:
    out: MLflowConfiguration = {}  # type: ignore[typeddict-item]
    if "MlflowResourceArn" in data:
        out["mlflow_resource_arn"] = data["MlflowResourceArn"]
    if "MlflowExperimentName" in data:
        out["mlflow_experiment_name"] = data["MlflowExperimentName"]
    return out
