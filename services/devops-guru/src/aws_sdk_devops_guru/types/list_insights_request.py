"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListInsightsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.list_insights_max_results
    import aws_sdk_devops_guru.types.list_insights_status_filter
    import aws_sdk_devops_guru.types.uuid_next_token


class ListInsightsRequest(TypedDict):
    status_filter: (
        "aws_sdk_devops_guru.types.list_insights_status_filter.ListInsightsStatusFilter"
    )
    """<p> A filter used to filter the returned insights by their status. You can specify one status filter. </p>"""
    max_results: NotRequired[
        "aws_sdk_devops_guru.types.list_insights_max_results.ListInsightsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsRequest) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.list_insights_status_filter

    out["StatusFilter"] = (
        aws_sdk_devops_guru.types.list_insights_status_filter.serialize_json(
            value["status_filter"]
        )
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInsightsRequest:
    out: ListInsightsRequest = {}  # type: ignore[typeddict-item]
    if "StatusFilter" in data:
        import aws_sdk_devops_guru.types.list_insights_status_filter

        out["status_filter"] = (
            aws_sdk_devops_guru.types.list_insights_status_filter.deserialize_json(
                data["StatusFilter"]
            )
        )
    else:
        raise DeserializationError("ListInsightsRequest.status_filter required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
