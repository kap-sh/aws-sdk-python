"""Generated from Smithy shape ``com.amazonaws.artifact#AccountSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_artifact.types.notification_subscription_status


class AccountSettings(TypedDict, closed=True):
    notification_subscription_status: NotRequired[
        "aws_sdk_artifact.types.notification_subscription_status.NotificationSubscriptionStatus"
    ]
    """<p>Notification subscription status of the customer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountSettings) -> dict:
    out: dict = {}
    if "notification_subscription_status" in value:
        import aws_sdk_artifact.types.notification_subscription_status

        out["notificationSubscriptionStatus"] = (
            aws_sdk_artifact.types.notification_subscription_status.serialize_json(
                value["notification_subscription_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccountSettings:
    out: AccountSettings = {}  # type: ignore[typeddict-item]
    if "notificationSubscriptionStatus" in data:
        import aws_sdk_artifact.types.notification_subscription_status

        out["notification_subscription_status"] = (
            aws_sdk_artifact.types.notification_subscription_status.deserialize_json(
                data["notificationSubscriptionStatus"]
            )
        )
    return out
