"""Generated from Smithy shape ``com.amazonaws.connect#SearchNotificationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.max_result100
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.notification_search_criteria
    import aws_sdk_connect.types.notification_search_filter


class SearchNotificationsRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response to retrieve the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page. Valid range is 1-100.</p>"""
    search_filter: NotRequired[
        "aws_sdk_connect.types.notification_search_filter.NotificationSearchFilter"
    ]
    """<p>Filters to apply to the search results, such as tag-based filters.</p>"""
    search_criteria: NotRequired[
        "aws_sdk_connect.types.notification_search_criteria.NotificationSearchCriteria"
    ]
    """<p>The search criteria to apply when searching for notifications. Supports filtering by notification ID and message content using comparison types such as STARTS_WITH, CONTAINS, and EXACT.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchNotificationsRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "search_filter" in value:
        import aws_sdk_connect.types.notification_search_filter

        out["SearchFilter"] = (
            aws_sdk_connect.types.notification_search_filter.serialize_json(
                value["search_filter"]
            )
        )
    if "search_criteria" in value:
        import aws_sdk_connect.types.notification_search_criteria

        out["SearchCriteria"] = (
            aws_sdk_connect.types.notification_search_criteria.serialize_json(
                value["search_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchNotificationsRequest:
    out: SearchNotificationsRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("SearchNotificationsRequest.instance_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "SearchFilter" in data:
        import aws_sdk_connect.types.notification_search_filter

        out["search_filter"] = (
            aws_sdk_connect.types.notification_search_filter.deserialize_json(
                data["SearchFilter"]
            )
        )
    if "SearchCriteria" in data:
        import aws_sdk_connect.types.notification_search_criteria

        out["search_criteria"] = (
            aws_sdk_connect.types.notification_search_criteria.deserialize_json(
                data["SearchCriteria"]
            )
        )
    return out
