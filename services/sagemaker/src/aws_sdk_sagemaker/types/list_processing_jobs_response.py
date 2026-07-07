"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListProcessingJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.processing_job_summaries


class ListProcessingJobsResponse(TypedDict, closed=True):
    processing_job_summaries: NotRequired[
        "aws_sdk_sagemaker.types.processing_job_summaries.ProcessingJobSummaries"
    ]
    """<p>An array of <code>ProcessingJobSummary</code> objects, each listing a processing job.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of processing jobs, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProcessingJobsResponse) -> dict:
    out: dict = {}
    if "processing_job_summaries" in value:
        import aws_sdk_sagemaker.types.processing_job_summaries

        out["ProcessingJobSummaries"] = (
            aws_sdk_sagemaker.types.processing_job_summaries.serialize_aws_json_1_1(
                value["processing_job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProcessingJobsResponse:
    out: ListProcessingJobsResponse = {}  # type: ignore[typeddict-item]
    if "ProcessingJobSummaries" in data:
        import aws_sdk_sagemaker.types.processing_job_summaries

        out["processing_job_summaries"] = (
            aws_sdk_sagemaker.types.processing_job_summaries.deserialize_aws_json_1_1(
                data["ProcessingJobSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
