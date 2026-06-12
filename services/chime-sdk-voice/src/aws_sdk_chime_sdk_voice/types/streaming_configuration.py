"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#StreamingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.boolean
    import aws_sdk_chime_sdk_voice.types.data_retention_in_hours
    import aws_sdk_chime_sdk_voice.types.media_insights_configuration
    import aws_sdk_chime_sdk_voice.types.streaming_notification_target_list


class StreamingConfiguration(TypedDict):
    data_retention_in_hours: (
        "aws_sdk_chime_sdk_voice.types.data_retention_in_hours.DataRetentionInHours"
    )
    """<p>The amount of time, in hours, to the Kinesis data.</p>"""
    disabled: "aws_sdk_chime_sdk_voice.types.boolean.Boolean"
    """<p>When true, streaming to Kinesis is off.</p>"""
    streaming_notification_targets: NotRequired[
        "aws_sdk_chime_sdk_voice.types.streaming_notification_target_list.StreamingNotificationTargetList"
    ]
    """<p>The streaming notification targets.</p>"""
    media_insights_configuration: NotRequired[
        "aws_sdk_chime_sdk_voice.types.media_insights_configuration.MediaInsightsConfiguration"
    ]
    """<p>The call analytics configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamingConfiguration) -> dict:
    out: dict = {}
    out["DataRetentionInHours"] = value["data_retention_in_hours"]
    out["Disabled"] = value["disabled"]
    if "streaming_notification_targets" in value:
        import aws_sdk_chime_sdk_voice.types.streaming_notification_target_list

        out["StreamingNotificationTargets"] = (
            aws_sdk_chime_sdk_voice.types.streaming_notification_target_list.serialize_json(
                value["streaming_notification_targets"]
            )
        )
    if "media_insights_configuration" in value:
        import aws_sdk_chime_sdk_voice.types.media_insights_configuration

        out["MediaInsightsConfiguration"] = (
            aws_sdk_chime_sdk_voice.types.media_insights_configuration.serialize_json(
                value["media_insights_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StreamingConfiguration:
    out: StreamingConfiguration = {}  # type: ignore[typeddict-item]
    if "DataRetentionInHours" in data:
        out["data_retention_in_hours"] = data["DataRetentionInHours"]
    else:
        raise DeserializationError(
            "StreamingConfiguration.data_retention_in_hours required"
        )
    if "Disabled" in data:
        out["disabled"] = data["Disabled"]
    else:
        raise DeserializationError("StreamingConfiguration.disabled required")
    if "StreamingNotificationTargets" in data:
        import aws_sdk_chime_sdk_voice.types.streaming_notification_target_list

        out["streaming_notification_targets"] = (
            aws_sdk_chime_sdk_voice.types.streaming_notification_target_list.deserialize_json(
                data["StreamingNotificationTargets"]
            )
        )
    if "MediaInsightsConfiguration" in data:
        import aws_sdk_chime_sdk_voice.types.media_insights_configuration

        out["media_insights_configuration"] = (
            aws_sdk_chime_sdk_voice.types.media_insights_configuration.deserialize_json(
                data["MediaInsightsConfiguration"]
            )
        )
    return out
