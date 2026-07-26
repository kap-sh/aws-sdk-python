"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTrainingPlanExtensionHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.training_plan_arn


class DescribeTrainingPlanExtensionHistoryRequest(TypedDict, closed=True):
    training_plan_arn: NotRequired[
        "capo_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    """<p>The Amazon Resource Name (ARN); of the training plan to retrieve extension history for.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token to continue pagination if more results are available.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of extensions to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrainingPlanExtensionHistoryRequest) -> dict:
    out: dict = {}
    if "training_plan_arn" in value:
        out["TrainingPlanArn"] = value["training_plan_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrainingPlanExtensionHistoryRequest:
    out: DescribeTrainingPlanExtensionHistoryRequest = {}  # type: ignore[typeddict-item]
    if "TrainingPlanArn" in data:
        out["training_plan_arn"] = data["TrainingPlanArn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
