"""Generated from Smithy shape ``com.amazonaws.sagemaker#MlflowDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.mlflow_experiment_id
    import aws_sdk_sagemaker.types.mlflow_run_id


class MlflowDetails(TypedDict):
    mlflow_experiment_id: NotRequired[
        "aws_sdk_sagemaker.types.mlflow_experiment_id.MlflowExperimentId"
    ]
    """<p> The MLflow experiment ID used for this job. </p>"""
    mlflow_run_id: NotRequired["aws_sdk_sagemaker.types.mlflow_run_id.MlflowRunId"]
    """<p> The MLflow run ID used for this job. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MlflowDetails) -> dict:
    out: dict = {}
    if "mlflow_experiment_id" in value:
        out["MlflowExperimentId"] = value["mlflow_experiment_id"]
    if "mlflow_run_id" in value:
        out["MlflowRunId"] = value["mlflow_run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MlflowDetails:
    out: MlflowDetails = {}  # type: ignore[typeddict-item]
    if "MlflowExperimentId" in data:
        out["mlflow_experiment_id"] = data["MlflowExperimentId"]
    if "MlflowRunId" in data:
        out["mlflow_run_id"] = data["MlflowRunId"]
    return out
