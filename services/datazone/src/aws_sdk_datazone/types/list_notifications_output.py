"""Generated from Smithy shape ``com.amazonaws.datazone#ListNotificationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.notifications_list
    import aws_sdk_datazone.types.pagination_token


class ListNotificationsOutput(TypedDict):
    notifications: NotRequired[
        "aws_sdk_datazone.types.notifications_list.NotificationsList"
    ]
    """<p>The results of the <code>ListNotifications</code> action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of notifications is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notifications, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotifications</code> to list the next set of notifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationsOutput) -> dict:
    out: dict = {}
    if "notifications" in value:
        import aws_sdk_datazone.types.notifications_list

        out["notifications"] = aws_sdk_datazone.types.notifications_list.serialize_json(
            value["notifications"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNotificationsOutput:
    out: ListNotificationsOutput = {}  # type: ignore[typeddict-item]
    if "notifications" in data:
        import aws_sdk_datazone.types.notifications_list

        out["notifications"] = (
            aws_sdk_datazone.types.notifications_list.deserialize_json(
                data["notifications"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
