"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListDependenciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.max_results
    import aws_sdk_resiliencehubv2.types.next_token
    import aws_sdk_resiliencehubv2.types.query_granularity


class ListDependenciesRequest(TypedDict, closed=True):
    service_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]
    query_range_start_time: NotRequired["datetime.datetime"]
    """<p>The start time for the dependency query range.</p>"""
    query_range_end_time: NotRequired["datetime.datetime"]
    """<p>The end time for the dependency query range.</p>"""
    query_range_granularity: NotRequired[
        "aws_sdk_resiliencehubv2.types.query_granularity.QueryGranularity"
    ]
    """<p>The granularity for the dependency query range.</p>"""
    max_results: "aws_sdk_resiliencehubv2.types.max_results.MaxResults"
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListDependenciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDependenciesRequest:
    out: ListDependenciesRequest = {}  # type: ignore[typeddict-item]
    return out
