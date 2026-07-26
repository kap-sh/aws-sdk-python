"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateMlflowAppResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.mlflow_app_arn


class UpdateMlflowAppResponse(TypedDict, closed=True):
    arn: NotRequired["capo_sagemaker.types.mlflow_app_arn.MlflowAppArn"]
    """<p>The ARN of the updated MLflow App.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMlflowAppResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMlflowAppResponse:
    out: UpdateMlflowAppResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
