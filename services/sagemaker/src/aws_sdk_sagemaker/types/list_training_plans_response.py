"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrainingPlansResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.training_plan_summaries


class ListTrainingPlansResponse(TypedDict):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token to continue pagination if more results are available.</p>"""
    training_plan_summaries: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_summaries.TrainingPlanSummaries"
    ]
    """<p>A list of summary information for the training plans.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrainingPlansResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "training_plan_summaries" in value:
        import aws_sdk_sagemaker.types.training_plan_summaries

        out["TrainingPlanSummaries"] = (
            aws_sdk_sagemaker.types.training_plan_summaries.serialize_aws_json_1_1(
                value["training_plan_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTrainingPlansResponse:
    out: ListTrainingPlansResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "TrainingPlanSummaries" in data:
        import aws_sdk_sagemaker.types.training_plan_summaries

        out["training_plan_summaries"] = (
            aws_sdk_sagemaker.types.training_plan_summaries.deserialize_aws_json_1_1(
                data["TrainingPlanSummaries"]
            )
        )
    return out
