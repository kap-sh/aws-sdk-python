"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrainingJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.training_job_summaries


class ListTrainingJobsResponse(TypedDict):
    training_job_summaries: NotRequired[
        "aws_sdk_sagemaker.types.training_job_summaries.TrainingJobSummaries"
    ]
    """<p>An array of <code>TrainingJobSummary</code> objects, each listing a training job.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of training jobs, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrainingJobsResponse) -> dict:
    out: dict = {}
    if "training_job_summaries" in value:
        import aws_sdk_sagemaker.types.training_job_summaries

        out["TrainingJobSummaries"] = (
            aws_sdk_sagemaker.types.training_job_summaries.serialize_aws_json_1_1(
                value["training_job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTrainingJobsResponse:
    out: ListTrainingJobsResponse = {}  # type: ignore[typeddict-item]
    if "TrainingJobSummaries" in data:
        import aws_sdk_sagemaker.types.training_job_summaries

        out["training_job_summaries"] = (
            aws_sdk_sagemaker.types.training_job_summaries.deserialize_aws_json_1_1(
                data["TrainingJobSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
