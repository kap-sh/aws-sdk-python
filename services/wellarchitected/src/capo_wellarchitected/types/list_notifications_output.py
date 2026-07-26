"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListNotificationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.notification_summaries


class ListNotificationsOutput(TypedDict, closed=True):
    notification_summaries: NotRequired[
        "capo_wellarchitected.types.notification_summaries.NotificationSummaries"
    ]
    """<p>List of lens notification summaries in a workload.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationsOutput) -> dict:
    out: dict = {}
    if "notification_summaries" in value:
        import capo_wellarchitected.types.notification_summaries

        out["NotificationSummaries"] = (
            capo_wellarchitected.types.notification_summaries.serialize_json(
                value["notification_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNotificationsOutput:
    out: ListNotificationsOutput = {}  # type: ignore[typeddict-item]
    if "NotificationSummaries" in data:
        import capo_wellarchitected.types.notification_summaries

        out["notification_summaries"] = (
            capo_wellarchitected.types.notification_summaries.deserialize_json(
                data["NotificationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
