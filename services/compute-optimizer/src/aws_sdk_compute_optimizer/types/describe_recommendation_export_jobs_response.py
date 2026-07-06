"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#DescribeRecommendationExportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.next_token
    import aws_sdk_compute_optimizer.types.recommendation_export_jobs


class DescribeRecommendationExportJobsResponse(TypedDict, closed=True):
    recommendation_export_jobs: NotRequired[
        "aws_sdk_compute_optimizer.types.recommendation_export_jobs.RecommendationExportJobs"
    ]
    """<p>An array of objects that describe recommendation export jobs.</p>"""
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to use to advance to the next page of export jobs.</p> <p>This value is null when there are no more pages of export jobs to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRecommendationExportJobsResponse) -> dict:
    out: dict = {}
    if "recommendation_export_jobs" in value:
        import aws_sdk_compute_optimizer.types.recommendation_export_jobs

        out["recommendationExportJobs"] = (
            aws_sdk_compute_optimizer.types.recommendation_export_jobs.serialize_aws_json_1_0(
                value["recommendation_export_jobs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRecommendationExportJobsResponse:
    out: DescribeRecommendationExportJobsResponse = {}  # type: ignore[typeddict-item]
    if "recommendationExportJobs" in data:
        import aws_sdk_compute_optimizer.types.recommendation_export_jobs

        out["recommendation_export_jobs"] = (
            aws_sdk_compute_optimizer.types.recommendation_export_jobs.deserialize_aws_json_1_0(
                data["recommendationExportJobs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
