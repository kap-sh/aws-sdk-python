"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListNotificationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.notifications
    import capo_auditmanager.types.token


class ListNotificationsResponse(TypedDict, closed=True):
    notifications: NotRequired["capo_auditmanager.types.notifications.Notifications"]
    """<p> The returned list of notifications. </p>"""
    next_token: NotRequired["capo_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationsResponse) -> dict:
    out: dict = {}
    if "notifications" in value:
        import capo_auditmanager.types.notifications

        out["notifications"] = capo_auditmanager.types.notifications.serialize_json(
            value["notifications"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNotificationsResponse:
    out: ListNotificationsResponse = {}  # type: ignore[typeddict-item]
    if "notifications" in data:
        import capo_auditmanager.types.notifications

        out["notifications"] = capo_auditmanager.types.notifications.deserialize_json(
            data["notifications"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
