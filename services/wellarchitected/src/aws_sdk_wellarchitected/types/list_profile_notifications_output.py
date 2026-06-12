"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListProfileNotificationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.profile_notification_summaries


class ListProfileNotificationsOutput(TypedDict):
    notification_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.profile_notification_summaries.ProfileNotificationSummaries"
    ]
    """<p>Notification summaries.</p>"""
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileNotificationsOutput) -> dict:
    out: dict = {}
    if "notification_summaries" in value:
        import aws_sdk_wellarchitected.types.profile_notification_summaries

        out["NotificationSummaries"] = (
            aws_sdk_wellarchitected.types.profile_notification_summaries.serialize_json(
                value["notification_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfileNotificationsOutput:
    out: ListProfileNotificationsOutput = {}  # type: ignore[typeddict-item]
    if "NotificationSummaries" in data:
        import aws_sdk_wellarchitected.types.profile_notification_summaries

        out["notification_summaries"] = (
            aws_sdk_wellarchitected.types.profile_notification_summaries.deserialize_json(
                data["NotificationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
