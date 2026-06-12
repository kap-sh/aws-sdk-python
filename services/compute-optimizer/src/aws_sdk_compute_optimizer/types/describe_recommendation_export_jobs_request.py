"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#DescribeRecommendationExportJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.job_filters
    import aws_sdk_compute_optimizer.types.job_ids
    import aws_sdk_compute_optimizer.types.max_results
    import aws_sdk_compute_optimizer.types.next_token


class DescribeRecommendationExportJobsRequest(TypedDict):
    job_ids: NotRequired["aws_sdk_compute_optimizer.types.job_ids.JobIds"]
    """<p>The identification numbers of the export jobs to return.</p> <p>An export job ID is returned when you create an export using the <a>ExportAutoScalingGroupRecommendations</a> or <a>ExportEC2InstanceRecommendations</a> actions.</p> <p>All export jobs created in the last seven days are returned if this parameter is omitted.</p>"""
    filters: NotRequired["aws_sdk_compute_optimizer.types.job_filters.JobFilters"]
    """<p>An array of objects to specify a filter that returns a more specific list of export jobs.</p>"""
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of export jobs.</p>"""
    max_results: NotRequired["aws_sdk_compute_optimizer.types.max_results.MaxResults"]
    """<p>The maximum number of export jobs to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRecommendationExportJobsRequest) -> dict:
    out: dict = {}
    if "job_ids" in value:
        import aws_sdk_compute_optimizer.types.job_ids

        out["jobIds"] = aws_sdk_compute_optimizer.types.job_ids.serialize_aws_json_1_0(
            value["job_ids"]
        )
    if "filters" in value:
        import aws_sdk_compute_optimizer.types.job_filters

        out["filters"] = (
            aws_sdk_compute_optimizer.types.job_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRecommendationExportJobsRequest:
    out: DescribeRecommendationExportJobsRequest = {}  # type: ignore[typeddict-item]
    if "jobIds" in data:
        import aws_sdk_compute_optimizer.types.job_ids

        out["job_ids"] = (
            aws_sdk_compute_optimizer.types.job_ids.deserialize_aws_json_1_0(
                data["jobIds"]
            )
        )
    if "filters" in data:
        import aws_sdk_compute_optimizer.types.job_filters

        out["filters"] = (
            aws_sdk_compute_optimizer.types.job_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
