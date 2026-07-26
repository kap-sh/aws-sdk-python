"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTransformJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.transform_job_summaries


class ListTransformJobsResponse(TypedDict, closed=True):
    transform_job_summaries: NotRequired[
        "capo_sagemaker.types.transform_job_summaries.TransformJobSummaries"
    ]
    """<p>An array of <code>TransformJobSummary</code> objects.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of transform jobs, use it in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTransformJobsResponse) -> dict:
    out: dict = {}
    if "transform_job_summaries" in value:
        import capo_sagemaker.types.transform_job_summaries

        out["TransformJobSummaries"] = (
            capo_sagemaker.types.transform_job_summaries.serialize_aws_json_1_1(
                value["transform_job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTransformJobsResponse:
    out: ListTransformJobsResponse = {}  # type: ignore[typeddict-item]
    if "TransformJobSummaries" in data:
        import capo_sagemaker.types.transform_job_summaries

        out["transform_job_summaries"] = (
            capo_sagemaker.types.transform_job_summaries.deserialize_aws_json_1_1(
                data["TransformJobSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
