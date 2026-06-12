"""Generated from Smithy shape ``com.amazonaws.connect#SearchNotificationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.approximate_total_count
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.notification_search_summary_list


class SearchNotificationsResponse(TypedDict):
    notifications: NotRequired[
        "aws_sdk_connect.types.notification_search_summary_list.NotificationSearchSummaryList"
    ]
    """<p>A list of notifications matching the search criteria.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. If present, there are more results available.</p>"""
    approximate_total_count: NotRequired[
        "aws_sdk_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The approximate total number of notifications matching the search criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchNotificationsResponse) -> dict:
    out: dict = {}
    if "notifications" in value:
        import aws_sdk_connect.types.notification_search_summary_list

        out["Notifications"] = (
            aws_sdk_connect.types.notification_search_summary_list.serialize_json(
                value["notifications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchNotificationsResponse:
    out: SearchNotificationsResponse = {}  # type: ignore[typeddict-item]
    if "Notifications" in data:
        import aws_sdk_connect.types.notification_search_summary_list

        out["notifications"] = (
            aws_sdk_connect.types.notification_search_summary_list.deserialize_json(
                data["Notifications"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
