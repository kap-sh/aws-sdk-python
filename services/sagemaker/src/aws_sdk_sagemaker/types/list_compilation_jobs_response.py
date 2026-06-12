"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListCompilationJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.compilation_job_summaries
    import aws_sdk_sagemaker.types.next_token


class ListCompilationJobsResponse(TypedDict):
    compilation_job_summaries: NotRequired[
        "aws_sdk_sagemaker.types.compilation_job_summaries.CompilationJobSummaries"
    ]
    """<p>An array of <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CompilationJobSummary.html\">CompilationJobSummary</a> objects, each describing a model compilation job. </p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon SageMaker AI returns this <code>NextToken</code>. To retrieve the next set of model compilation jobs, use this token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCompilationJobsResponse) -> dict:
    out: dict = {}
    if "compilation_job_summaries" in value:
        import aws_sdk_sagemaker.types.compilation_job_summaries

        out["CompilationJobSummaries"] = (
            aws_sdk_sagemaker.types.compilation_job_summaries.serialize_aws_json_1_1(
                value["compilation_job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCompilationJobsResponse:
    out: ListCompilationJobsResponse = {}  # type: ignore[typeddict-item]
    if "CompilationJobSummaries" in data:
        import aws_sdk_sagemaker.types.compilation_job_summaries

        out["compilation_job_summaries"] = (
            aws_sdk_sagemaker.types.compilation_job_summaries.deserialize_aws_json_1_1(
                data["CompilationJobSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
