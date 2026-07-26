"""Generated from Smithy shape ``com.amazonaws.notifications#GetNotificationsAccessForOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.notifications_access_for_organization


class GetNotificationsAccessForOrganizationResponse(TypedDict, closed=True):
    notifications_access_for_organization: "capo_notifications.types.notifications_access_for_organization.NotificationsAccessForOrganization"
    """<p>The <code>AccessStatus</code> of Service Trust Enablement for User Notifications to Amazon Web Services Organizations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotificationsAccessForOrganizationResponse) -> dict:
    out: dict = {}
    import capo_notifications.types.notifications_access_for_organization

    out["notificationsAccessForOrganization"] = (
        capo_notifications.types.notifications_access_for_organization.serialize_json(
            value["notifications_access_for_organization"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetNotificationsAccessForOrganizationResponse:
    out: GetNotificationsAccessForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "notificationsAccessForOrganization" in data:
        import capo_notifications.types.notifications_access_for_organization

        out["notifications_access_for_organization"] = (
            capo_notifications.types.notifications_access_for_organization.deserialize_json(
                data["notificationsAccessForOrganization"]
            )
        )
    else:
        raise DeserializationError(
            "GetNotificationsAccessForOrganizationResponse.notifications_access_for_organization required"
        )
    return out
