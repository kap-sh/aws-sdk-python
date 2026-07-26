"""Generated from Smithy shape ``com.amazonaws.securitylake#NotificationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securitylake.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securitylake.types.https_notification_configuration
    import capo_securitylake.types.sqs_notification_configuration


class _NotificationConfiguration_sqsNotificationConfiguration(TypedDict, closed=True):
    sqsNotificationConfiguration: "capo_securitylake.types.sqs_notification_configuration.SqsNotificationConfiguration"


class _NotificationConfiguration_httpsNotificationConfiguration(TypedDict, closed=True):
    httpsNotificationConfiguration: "capo_securitylake.types.https_notification_configuration.HttpsNotificationConfiguration"


NotificationConfiguration: TypeAlias = (
    _NotificationConfiguration_sqsNotificationConfiguration
    | _NotificationConfiguration_httpsNotificationConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: NotificationConfiguration) -> dict:
    if "sqsNotificationConfiguration" in value:
        import capo_securitylake.types.sqs_notification_configuration

        return {
            "sqsNotificationConfiguration": capo_securitylake.types.sqs_notification_configuration.serialize_json(
                value["sqsNotificationConfiguration"]
            )
        }
    elif "httpsNotificationConfiguration" in value:
        import capo_securitylake.types.https_notification_configuration

        return {
            "httpsNotificationConfiguration": capo_securitylake.types.https_notification_configuration.serialize_json(
                value["httpsNotificationConfiguration"]
            )
        }
    else:
        raise SerializationError("NotificationConfiguration: no variant present")


def deserialize_json(data: dict) -> NotificationConfiguration:
    if "sqsNotificationConfiguration" in data:
        import capo_securitylake.types.sqs_notification_configuration

        return {
            "sqsNotificationConfiguration": capo_securitylake.types.sqs_notification_configuration.deserialize_json(
                data["sqsNotificationConfiguration"]
            )
        }
    elif "httpsNotificationConfiguration" in data:
        import capo_securitylake.types.https_notification_configuration

        return {
            "httpsNotificationConfiguration": capo_securitylake.types.https_notification_configuration.deserialize_json(
                data["httpsNotificationConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "NotificationConfiguration: no recognized variant key"
        )
