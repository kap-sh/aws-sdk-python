"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeMlflowAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.mlflow_app_arn


class DescribeMlflowAppRequest(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_sagemaker.types.mlflow_app_arn.MlflowAppArn"]
    """<p>The ARN of the MLflow App for which to get information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMlflowAppRequest) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMlflowAppRequest:
    out: DescribeMlflowAppRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
