"""Generated from Smithy shape ``com.amazonaws.notifications#AssociateManagedNotificationAccountContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.account_contact_type
    import aws_sdk_notifications.types.managed_notification_configuration_os_arn


class AssociateManagedNotificationAccountContactRequest(TypedDict):
    contact_identifier: (
        "aws_sdk_notifications.types.account_contact_type.AccountContactType"
    )
    """<p>A unique value of an Account Contact Type to associate with the <code>ManagedNotificationConfiguration</code>.</p>"""
    managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the Account Contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateManagedNotificationAccountContactRequest) -> dict:
    out: dict = {}
    out["managedNotificationConfigurationArn"] = value[
        "managed_notification_configuration_arn"
    ]
    return out


def deserialize_json(data: dict) -> AssociateManagedNotificationAccountContactRequest:
    out: AssociateManagedNotificationAccountContactRequest = {}  # type: ignore[typeddict-item]
    if "managedNotificationConfigurationArn" in data:
        out["managed_notification_configuration_arn"] = data[
            "managedNotificationConfigurationArn"
        ]
    else:
        raise DeserializationError(
            "AssociateManagedNotificationAccountContactRequest.managed_notification_configuration_arn required"
        )
    return out
