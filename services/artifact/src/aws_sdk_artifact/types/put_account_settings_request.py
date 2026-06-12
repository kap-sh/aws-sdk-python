"""Generated from Smithy shape ``com.amazonaws.artifact#PutAccountSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_artifact.types.notification_subscription_status


class PutAccountSettingsRequest(TypedDict):
    notification_subscription_status: NotRequired[
        "aws_sdk_artifact.types.notification_subscription_status.NotificationSubscriptionStatus"
    ]
    """<p>Desired notification subscription status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountSettingsRequest) -> dict:
    out: dict = {}
    if "notification_subscription_status" in value:
        import aws_sdk_artifact.types.notification_subscription_status

        out["notificationSubscriptionStatus"] = (
            aws_sdk_artifact.types.notification_subscription_status.serialize_json(
                value["notification_subscription_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutAccountSettingsRequest:
    out: PutAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    if "notificationSubscriptionStatus" in data:
        import aws_sdk_artifact.types.notification_subscription_status

        out["notification_subscription_status"] = (
            aws_sdk_artifact.types.notification_subscription_status.deserialize_json(
                data["notificationSubscriptionStatus"]
            )
        )
    return out
