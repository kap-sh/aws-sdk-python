"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrainingPlansResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.training_plan_summaries


class ListTrainingPlansResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token to continue pagination if more results are available.</p>"""
    training_plan_summaries: NotRequired[
        "capo_sagemaker.types.training_plan_summaries.TrainingPlanSummaries"
    ]
    """<p>A list of summary information for the training plans.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrainingPlansResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "training_plan_summaries" in value:
        import capo_sagemaker.types.training_plan_summaries

        out["TrainingPlanSummaries"] = (
            capo_sagemaker.types.training_plan_summaries.serialize_aws_json_1_1(
                value["training_plan_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTrainingPlansResponse:
    out: ListTrainingPlansResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "TrainingPlanSummaries" in data:
        import capo_sagemaker.types.training_plan_summaries

        out["training_plan_summaries"] = (
            capo_sagemaker.types.training_plan_summaries.deserialize_aws_json_1_1(
                data["TrainingPlanSummaries"]
            )
        )
    return out
