"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListEventsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.aws_account_id
    import aws_sdk_devops_guru.types.list_events_filters
    import aws_sdk_devops_guru.types.list_events_max_results
    import aws_sdk_devops_guru.types.uuid_next_token


class ListEventsRequest(TypedDict):
    filters: "aws_sdk_devops_guru.types.list_events_filters.ListEventsFilters"
    """<p> A <code>ListEventsFilters</code> object used to specify which events to return. </p>"""
    max_results: NotRequired[
        "aws_sdk_devops_guru.types.list_events_max_results.ListEventsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""
    account_id: NotRequired["aws_sdk_devops_guru.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventsRequest) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.list_events_filters

    out["Filters"] = aws_sdk_devops_guru.types.list_events_filters.serialize_json(
        value["filters"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ListEventsRequest:
    out: ListEventsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_devops_guru.types.list_events_filters

        out["filters"] = aws_sdk_devops_guru.types.list_events_filters.deserialize_json(
            data["Filters"]
        )
    else:
        raise DeserializationError("ListEventsRequest.filters required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    return out
