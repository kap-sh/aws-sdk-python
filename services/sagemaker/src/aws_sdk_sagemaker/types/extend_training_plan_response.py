"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExtendTrainingPlanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_plan_extensions


class ExtendTrainingPlanResponse(TypedDict, closed=True):
    training_plan_extensions: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_extensions.TrainingPlanExtensions"
    ]
    """<p>The list of extensions for the training plan, including the newly created extension.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtendTrainingPlanResponse) -> dict:
    out: dict = {}
    if "training_plan_extensions" in value:
        import aws_sdk_sagemaker.types.training_plan_extensions

        out["TrainingPlanExtensions"] = (
            aws_sdk_sagemaker.types.training_plan_extensions.serialize_aws_json_1_1(
                value["training_plan_extensions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtendTrainingPlanResponse:
    out: ExtendTrainingPlanResponse = {}  # type: ignore[typeddict-item]
    if "TrainingPlanExtensions" in data:
        import aws_sdk_sagemaker.types.training_plan_extensions

        out["training_plan_extensions"] = (
            aws_sdk_sagemaker.types.training_plan_extensions.deserialize_aws_json_1_1(
                data["TrainingPlanExtensions"]
            )
        )
    return out
