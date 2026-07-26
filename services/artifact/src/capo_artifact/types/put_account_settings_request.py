"""Generated from Smithy shape ``com.amazonaws.artifact#PutAccountSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.notification_subscription_status


class PutAccountSettingsRequest(TypedDict, closed=True):
    notification_subscription_status: NotRequired[
        "capo_artifact.types.notification_subscription_status.NotificationSubscriptionStatus"
    ]
    """<p>Desired notification subscription status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountSettingsRequest) -> dict:
    out: dict = {}
    if "notification_subscription_status" in value:
        import capo_artifact.types.notification_subscription_status

        out["notificationSubscriptionStatus"] = (
            capo_artifact.types.notification_subscription_status.serialize_json(
                value["notification_subscription_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutAccountSettingsRequest:
    out: PutAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    if "notificationSubscriptionStatus" in data:
        import capo_artifact.types.notification_subscription_status

        out["notification_subscription_status"] = (
            capo_artifact.types.notification_subscription_status.deserialize_json(
                data["notificationSubscriptionStatus"]
            )
        )
    return out
