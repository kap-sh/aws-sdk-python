"""Generated from Smithy shape ``com.amazonaws.glue#ListDataQualityStatisticAnnotationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.page_size
    import aws_sdk_glue.types.pagination_token
    import aws_sdk_glue.types.timestamp_filter


class ListDataQualityStatisticAnnotationsRequest(TypedDict):
    statistic_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The Statistic ID.</p>"""
    profile_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The Profile ID.</p>"""
    timestamp_filter: NotRequired["aws_sdk_glue.types.timestamp_filter.TimestampFilter"]
    """<p>A timestamp filter.</p>"""
    max_results: NotRequired["aws_sdk_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return in this request.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataQualityStatisticAnnotationsRequest) -> dict:
    out: dict = {}
    if "statistic_id" in value:
        out["StatisticId"] = value["statistic_id"]
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "timestamp_filter" in value:
        import aws_sdk_glue.types.timestamp_filter

        out["TimestampFilter"] = (
            aws_sdk_glue.types.timestamp_filter.serialize_aws_json_1_1(
                value["timestamp_filter"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataQualityStatisticAnnotationsRequest:
    out: ListDataQualityStatisticAnnotationsRequest = {}  # type: ignore[typeddict-item]
    if "StatisticId" in data:
        out["statistic_id"] = data["StatisticId"]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    if "TimestampFilter" in data:
        import aws_sdk_glue.types.timestamp_filter

        out["timestamp_filter"] = (
            aws_sdk_glue.types.timestamp_filter.deserialize_aws_json_1_1(
                data["TimestampFilter"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
