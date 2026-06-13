"""Generated from Smithy shape ``com.amazonaws.securitylake#CreateSubscriberNotificationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.notification_configuration
    import aws_sdk_securitylake.types.uuid


class CreateSubscriberNotificationRequest(TypedDict):
    subscriber_id: "aws_sdk_securitylake.types.uuid.UUID"
    """<p>The subscriber ID for the notification subscription.</p>"""
    configuration: "aws_sdk_securitylake.types.notification_configuration.NotificationConfiguration"
    """<p>Specify the configuration using which you want to create the subscriber notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriberNotificationRequest) -> dict:
    out: dict = {}
    import aws_sdk_securitylake.types.notification_configuration

    out["configuration"] = (
        aws_sdk_securitylake.types.notification_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateSubscriberNotificationRequest:
    out: CreateSubscriberNotificationRequest = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_securitylake.types.notification_configuration

        out["configuration"] = (
            aws_sdk_securitylake.types.notification_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSubscriberNotificationRequest.configuration required"
        )
    return out
