"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTrainingPlanResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_plan_arn


class CreateTrainingPlanResponse(TypedDict):
    training_plan_arn: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    """<p>The Amazon Resource Name (ARN); of the created training plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrainingPlanResponse) -> dict:
    out: dict = {}
    if "training_plan_arn" in value:
        out["TrainingPlanArn"] = value["training_plan_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrainingPlanResponse:
    out: CreateTrainingPlanResponse = {}  # type: ignore[typeddict-item]
    if "TrainingPlanArn" in data:
        out["training_plan_arn"] = data["TrainingPlanArn"]
    return out
