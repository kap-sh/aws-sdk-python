"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEdgePackagingJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.edge_packaging_job_summaries
    import aws_sdk_sagemaker.types.next_token


class ListEdgePackagingJobsResponse(TypedDict, closed=True):
    edge_packaging_job_summaries: NotRequired[
        "aws_sdk_sagemaker.types.edge_packaging_job_summaries.EdgePackagingJobSummaries"
    ]
    """<p>Summaries of edge packaging jobs.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>Token to use when calling the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEdgePackagingJobsResponse) -> dict:
    out: dict = {}
    if "edge_packaging_job_summaries" in value:
        import aws_sdk_sagemaker.types.edge_packaging_job_summaries

        out["EdgePackagingJobSummaries"] = (
            aws_sdk_sagemaker.types.edge_packaging_job_summaries.serialize_aws_json_1_1(
                value["edge_packaging_job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEdgePackagingJobsResponse:
    out: ListEdgePackagingJobsResponse = {}  # type: ignore[typeddict-item]
    if "EdgePackagingJobSummaries" in data:
        import aws_sdk_sagemaker.types.edge_packaging_job_summaries

        out["edge_packaging_job_summaries"] = (
            aws_sdk_sagemaker.types.edge_packaging_job_summaries.deserialize_aws_json_1_1(
                data["EdgePackagingJobSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
