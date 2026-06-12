"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTrainingPlanRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_plan_name


class DescribeTrainingPlanRequest(TypedDict):
    training_plan_name: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_name.TrainingPlanName"
    ]
    """<p>The name of the training plan to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrainingPlanRequest) -> dict:
    out: dict = {}
    if "training_plan_name" in value:
        out["TrainingPlanName"] = value["training_plan_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrainingPlanRequest:
    out: DescribeTrainingPlanRequest = {}  # type: ignore[typeddict-item]
    if "TrainingPlanName" in data:
        out["training_plan_name"] = data["TrainingPlanName"]
    return out
