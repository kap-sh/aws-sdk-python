"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#GetNotificationConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.notification_configuration


class GetNotificationConfigurationResponse(TypedDict):
    notification_configuration: "aws_sdk_codeguruprofiler.types.notification_configuration.NotificationConfiguration"
    """<p>The current notification configuration for this profiling group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotificationConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_codeguruprofiler.types.notification_configuration

    out["notificationConfiguration"] = (
        aws_sdk_codeguruprofiler.types.notification_configuration.serialize_json(
            value["notification_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetNotificationConfigurationResponse:
    out: GetNotificationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "notificationConfiguration" in data:
        import aws_sdk_codeguruprofiler.types.notification_configuration

        out["notification_configuration"] = (
            aws_sdk_codeguruprofiler.types.notification_configuration.deserialize_json(
                data["notificationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetNotificationConfigurationResponse.notification_configuration required"
        )
    return out
