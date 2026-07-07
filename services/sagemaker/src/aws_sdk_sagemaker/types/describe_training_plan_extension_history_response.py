"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTrainingPlanExtensionHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.training_plan_extensions


class DescribeTrainingPlanExtensionHistoryResponse(TypedDict, closed=True):
    training_plan_extensions: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_extensions.TrainingPlanExtensions"
    ]
    """<p>A list of extensions for the specified training plan.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token to continue pagination if more results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrainingPlanExtensionHistoryResponse) -> dict:
    out: dict = {}
    if "training_plan_extensions" in value:
        import aws_sdk_sagemaker.types.training_plan_extensions

        out["TrainingPlanExtensions"] = (
            aws_sdk_sagemaker.types.training_plan_extensions.serialize_aws_json_1_1(
                value["training_plan_extensions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeTrainingPlanExtensionHistoryResponse:
    out: DescribeTrainingPlanExtensionHistoryResponse = {}  # type: ignore[typeddict-item]
    if "TrainingPlanExtensions" in data:
        import aws_sdk_sagemaker.types.training_plan_extensions

        out["training_plan_extensions"] = (
            aws_sdk_sagemaker.types.training_plan_extensions.deserialize_aws_json_1_1(
                data["TrainingPlanExtensions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
