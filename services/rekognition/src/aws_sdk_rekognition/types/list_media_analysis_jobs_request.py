"""Generated from Smithy shape ``com.amazonaws.rekognition#ListMediaAnalysisJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.extended_pagination_token
    import aws_sdk_rekognition.types.list_media_analysis_jobs_page_size


class ListMediaAnalysisJobsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>Pagination token, if the previous response was incomplete.</p>"""
    max_results: NotRequired[
        "aws_sdk_rekognition.types.list_media_analysis_jobs_page_size.ListMediaAnalysisJobsPageSize"
    ]
    """<p>The maximum number of results to return per paginated call. The largest value user can specify is 100. If user specifies a value greater than 100, an <code>InvalidParameterException</code> error occurs. The default value is 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMediaAnalysisJobsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMediaAnalysisJobsRequest:
    out: ListMediaAnalysisJobsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
