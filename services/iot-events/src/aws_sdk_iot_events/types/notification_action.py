"""Generated from Smithy shape ``com.amazonaws.iotevents#NotificationAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.email_configurations
    import aws_sdk_iot_events.types.notification_target_actions
    import aws_sdk_iot_events.types.sms_configurations


class NotificationAction(TypedDict):
    action: (
        "aws_sdk_iot_events.types.notification_target_actions.NotificationTargetActions"
    )
    """<p>Specifies an AWS Lambda function to manage alarm notifications. You can create one or use the <a href=\"https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html\">AWS Lambda function provided by AWS IoT Events</a>.</p>"""
    sms_configurations: NotRequired[
        "aws_sdk_iot_events.types.sms_configurations.SMSConfigurations"
    ]
    """<p>Contains the configuration information of SMS notifications.</p>"""
    email_configurations: NotRequired[
        "aws_sdk_iot_events.types.email_configurations.EmailConfigurations"
    ]
    """<p>Contains the configuration information of email notifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationAction) -> dict:
    out: dict = {}
    import aws_sdk_iot_events.types.notification_target_actions

    out["action"] = aws_sdk_iot_events.types.notification_target_actions.serialize_json(
        value["action"]
    )
    if "sms_configurations" in value:
        import aws_sdk_iot_events.types.sms_configurations

        out["smsConfigurations"] = (
            aws_sdk_iot_events.types.sms_configurations.serialize_json(
                value["sms_configurations"]
            )
        )
    if "email_configurations" in value:
        import aws_sdk_iot_events.types.email_configurations

        out["emailConfigurations"] = (
            aws_sdk_iot_events.types.email_configurations.serialize_json(
                value["email_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> NotificationAction:
    out: NotificationAction = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_iot_events.types.notification_target_actions

        out["action"] = (
            aws_sdk_iot_events.types.notification_target_actions.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("NotificationAction.action required")
    if "smsConfigurations" in data:
        import aws_sdk_iot_events.types.sms_configurations

        out["sms_configurations"] = (
            aws_sdk_iot_events.types.sms_configurations.deserialize_json(
                data["smsConfigurations"]
            )
        )
    if "emailConfigurations" in data:
        import aws_sdk_iot_events.types.email_configurations

        out["email_configurations"] = (
            aws_sdk_iot_events.types.email_configurations.deserialize_json(
                data["emailConfigurations"]
            )
        )
    return out
