"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListHyperParameterTuningJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_summaries
    import aws_sdk_sagemaker.types.next_token


class ListHyperParameterTuningJobsResponse(TypedDict):
    hyper_parameter_tuning_job_summaries: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_summaries.HyperParameterTuningJobSummaries"
    ]
    """<p>A list of <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobSummary.html\">HyperParameterTuningJobSummary</a> objects that describe the tuning jobs that the <code>ListHyperParameterTuningJobs</code> request returned.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of this <code>ListHyperParameterTuningJobs</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of tuning jobs, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHyperParameterTuningJobsResponse) -> dict:
    out: dict = {}
    if "hyper_parameter_tuning_job_summaries" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_summaries

        out["HyperParameterTuningJobSummaries"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_summaries.serialize_aws_json_1_1(
                value["hyper_parameter_tuning_job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHyperParameterTuningJobsResponse:
    out: ListHyperParameterTuningJobsResponse = {}  # type: ignore[typeddict-item]
    if "HyperParameterTuningJobSummaries" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_summaries

        out["hyper_parameter_tuning_job_summaries"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_summaries.deserialize_aws_json_1_1(
                data["HyperParameterTuningJobSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
