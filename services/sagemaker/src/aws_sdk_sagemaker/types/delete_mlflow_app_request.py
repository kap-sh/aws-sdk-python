"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteMlflowAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.mlflow_app_arn


class DeleteMlflowAppRequest(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_sagemaker.types.mlflow_app_arn.MlflowAppArn"]
    """<p>The ARN of the MLflow App to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMlflowAppRequest) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMlflowAppRequest:
    out: DeleteMlflowAppRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
