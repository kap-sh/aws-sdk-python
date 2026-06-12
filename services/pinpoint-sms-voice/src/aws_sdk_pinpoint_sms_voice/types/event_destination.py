"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#EventDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.boolean
    import aws_sdk_pinpoint_sms_voice.types.cloud_watch_logs_destination
    import aws_sdk_pinpoint_sms_voice.types.event_types
    import aws_sdk_pinpoint_sms_voice.types.kinesis_firehose_destination
    import aws_sdk_pinpoint_sms_voice.types.sns_destination
    import aws_sdk_pinpoint_sms_voice.types.string


class EventDestination(TypedDict):
    cloud_watch_logs_destination: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.cloud_watch_logs_destination.CloudWatchLogsDestination"
    ]
    enabled: NotRequired["aws_sdk_pinpoint_sms_voice.types.boolean.Boolean"]
    """Indicates whether or not the event destination is enabled. If the event destination is enabled, then Amazon Pinpoint sends response data to the specified event destination."""
    kinesis_firehose_destination: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.kinesis_firehose_destination.KinesisFirehoseDestination"
    ]
    matching_event_types: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.event_types.EventTypes"
    ]
    name: NotRequired["aws_sdk_pinpoint_sms_voice.types.string.String"]
    """A name that identifies the event destination configuration."""
    sns_destination: NotRequired[
        "aws_sdk_pinpoint_sms_voice.types.sns_destination.SnsDestination"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: EventDestination) -> dict:
    out: dict = {}
    if "cloud_watch_logs_destination" in value:
        import aws_sdk_pinpoint_sms_voice.types.cloud_watch_logs_destination

        out["CloudWatchLogsDestination"] = (
            aws_sdk_pinpoint_sms_voice.types.cloud_watch_logs_destination.serialize_json(
                value["cloud_watch_logs_destination"]
            )
        )
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "kinesis_firehose_destination" in value:
        import aws_sdk_pinpoint_sms_voice.types.kinesis_firehose_destination

        out["KinesisFirehoseDestination"] = (
            aws_sdk_pinpoint_sms_voice.types.kinesis_firehose_destination.serialize_json(
                value["kinesis_firehose_destination"]
            )
        )
    if "matching_event_types" in value:
        import aws_sdk_pinpoint_sms_voice.types.event_types

        out["MatchingEventTypes"] = (
            aws_sdk_pinpoint_sms_voice.types.event_types.serialize_json(
                value["matching_event_types"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "sns_destination" in value:
        import aws_sdk_pinpoint_sms_voice.types.sns_destination

        out["SnsDestination"] = (
            aws_sdk_pinpoint_sms_voice.types.sns_destination.serialize_json(
                value["sns_destination"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventDestination:
    out: EventDestination = {}  # type: ignore[typeddict-item]
    if "CloudWatchLogsDestination" in data:
        import aws_sdk_pinpoint_sms_voice.types.cloud_watch_logs_destination

        out["cloud_watch_logs_destination"] = (
            aws_sdk_pinpoint_sms_voice.types.cloud_watch_logs_destination.deserialize_json(
                data["CloudWatchLogsDestination"]
            )
        )
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "KinesisFirehoseDestination" in data:
        import aws_sdk_pinpoint_sms_voice.types.kinesis_firehose_destination

        out["kinesis_firehose_destination"] = (
            aws_sdk_pinpoint_sms_voice.types.kinesis_firehose_destination.deserialize_json(
                data["KinesisFirehoseDestination"]
            )
        )
    if "MatchingEventTypes" in data:
        import aws_sdk_pinpoint_sms_voice.types.event_types

        out["matching_event_types"] = (
            aws_sdk_pinpoint_sms_voice.types.event_types.deserialize_json(
                data["MatchingEventTypes"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "SnsDestination" in data:
        import aws_sdk_pinpoint_sms_voice.types.sns_destination

        out["sns_destination"] = (
            aws_sdk_pinpoint_sms_voice.types.sns_destination.deserialize_json(
                data["SnsDestination"]
            )
        )
    return out
