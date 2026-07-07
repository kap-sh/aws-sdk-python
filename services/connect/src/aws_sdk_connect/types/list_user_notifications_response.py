"""Generated from Smithy shape ``com.amazonaws.connect#ListUserNotificationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.user_notification_summary_list


class ListUserNotificationsResponse(TypedDict, closed=True):
    user_notifications: NotRequired[
        "aws_sdk_connect.types.user_notification_summary_list.UserNotificationSummaryList"
    ]
    """<p>A list of notifications sent to the specified user.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. If present, there are more results available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUserNotificationsResponse) -> dict:
    out: dict = {}
    if "user_notifications" in value:
        import aws_sdk_connect.types.user_notification_summary_list

        out["UserNotifications"] = (
            aws_sdk_connect.types.user_notification_summary_list.serialize_json(
                value["user_notifications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUserNotificationsResponse:
    out: ListUserNotificationsResponse = {}  # type: ignore[typeddict-item]
    if "UserNotifications" in data:
        import aws_sdk_connect.types.user_notification_summary_list

        out["user_notifications"] = (
            aws_sdk_connect.types.user_notification_summary_list.deserialize_json(
                data["UserNotifications"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
