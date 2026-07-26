"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListProfileNotificationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.profile_notification_summaries


class ListProfileNotificationsOutput(TypedDict, closed=True):
    notification_summaries: NotRequired[
        "capo_wellarchitected.types.profile_notification_summaries.ProfileNotificationSummaries"
    ]
    """<p>Notification summaries.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileNotificationsOutput) -> dict:
    out: dict = {}
    if "notification_summaries" in value:
        import capo_wellarchitected.types.profile_notification_summaries

        out["NotificationSummaries"] = (
            capo_wellarchitected.types.profile_notification_summaries.serialize_json(
                value["notification_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfileNotificationsOutput:
    out: ListProfileNotificationsOutput = {}  # type: ignore[typeddict-item]
    if "NotificationSummaries" in data:
        import capo_wellarchitected.types.profile_notification_summaries

        out["notification_summaries"] = (
            capo_wellarchitected.types.profile_notification_summaries.deserialize_json(
                data["NotificationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
