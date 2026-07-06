"""Generated from Smithy shape ``com.amazonaws.securitylake#UpdateSubscriberNotificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.notification_configuration
    import aws_sdk_securitylake.types.uuid


class UpdateSubscriberNotificationRequest(TypedDict, closed=True):
    subscriber_id: "aws_sdk_securitylake.types.uuid.UUID"
    """<p>The subscription ID for which the subscription notification is specified.</p>"""
    configuration: "aws_sdk_securitylake.types.notification_configuration.NotificationConfiguration"
    """<p>The configuration for subscriber notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSubscriberNotificationRequest) -> dict:
    out: dict = {}
    import aws_sdk_securitylake.types.notification_configuration

    out["configuration"] = (
        aws_sdk_securitylake.types.notification_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateSubscriberNotificationRequest:
    out: UpdateSubscriberNotificationRequest = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_securitylake.types.notification_configuration

        out["configuration"] = (
            aws_sdk_securitylake.types.notification_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSubscriberNotificationRequest.configuration required"
        )
    return out
