"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteMlflowAppResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.mlflow_app_arn


class DeleteMlflowAppResponse(TypedDict, closed=True):
    arn: NotRequired["capo_sagemaker.types.mlflow_app_arn.MlflowAppArn"]
    """<p>The ARN of the deleted MLflow App.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMlflowAppResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMlflowAppResponse:
    out: DeleteMlflowAppResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
