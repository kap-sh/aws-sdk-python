"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#NotificationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.configuration_status
    import aws_sdk_kinesis_video.types.notification_destination_config


class NotificationConfiguration(TypedDict, closed=True):
    status: "aws_sdk_kinesis_video.types.configuration_status.ConfigurationStatus"
    """<p>Indicates if a notification configuration is enabled or disabled.</p>"""
    destination_config: "aws_sdk_kinesis_video.types.notification_destination_config.NotificationDestinationConfig"
    """<p>The destination information required to deliver a notification to a customer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_video.types.configuration_status

    out["Status"] = aws_sdk_kinesis_video.types.configuration_status.serialize_json(
        value["status"]
    )
    import aws_sdk_kinesis_video.types.notification_destination_config

    out["DestinationConfig"] = (
        aws_sdk_kinesis_video.types.notification_destination_config.serialize_json(
            value["destination_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> NotificationConfiguration:
    out: NotificationConfiguration = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_kinesis_video.types.configuration_status

        out["status"] = (
            aws_sdk_kinesis_video.types.configuration_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("NotificationConfiguration.status required")
    if "DestinationConfig" in data:
        import aws_sdk_kinesis_video.types.notification_destination_config

        out["destination_config"] = (
            aws_sdk_kinesis_video.types.notification_destination_config.deserialize_json(
                data["DestinationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "NotificationConfiguration.destination_config required"
        )
    return out
