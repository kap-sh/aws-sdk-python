"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#EventDestinationDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice.types.boolean
    import capo_pinpoint_sms_voice.types.cloud_watch_logs_destination
    import capo_pinpoint_sms_voice.types.event_types
    import capo_pinpoint_sms_voice.types.kinesis_firehose_destination
    import capo_pinpoint_sms_voice.types.sns_destination


class EventDestinationDefinition(TypedDict, closed=True):
    cloud_watch_logs_destination: NotRequired[
        "capo_pinpoint_sms_voice.types.cloud_watch_logs_destination.CloudWatchLogsDestination"
    ]
    enabled: NotRequired["capo_pinpoint_sms_voice.types.boolean.Boolean"]
    """Indicates whether or not the event destination is enabled. If the event destination is enabled, then Amazon Pinpoint sends response data to the specified event destination."""
    kinesis_firehose_destination: NotRequired[
        "capo_pinpoint_sms_voice.types.kinesis_firehose_destination.KinesisFirehoseDestination"
    ]
    matching_event_types: NotRequired[
        "capo_pinpoint_sms_voice.types.event_types.EventTypes"
    ]
    sns_destination: NotRequired[
        "capo_pinpoint_sms_voice.types.sns_destination.SnsDestination"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: EventDestinationDefinition) -> dict:
    out: dict = {}
    if "cloud_watch_logs_destination" in value:
        import capo_pinpoint_sms_voice.types.cloud_watch_logs_destination

        out["CloudWatchLogsDestination"] = (
            capo_pinpoint_sms_voice.types.cloud_watch_logs_destination.serialize_json(
                value["cloud_watch_logs_destination"]
            )
        )
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "kinesis_firehose_destination" in value:
        import capo_pinpoint_sms_voice.types.kinesis_firehose_destination

        out["KinesisFirehoseDestination"] = (
            capo_pinpoint_sms_voice.types.kinesis_firehose_destination.serialize_json(
                value["kinesis_firehose_destination"]
            )
        )
    if "matching_event_types" in value:
        import capo_pinpoint_sms_voice.types.event_types

        out["MatchingEventTypes"] = (
            capo_pinpoint_sms_voice.types.event_types.serialize_json(
                value["matching_event_types"]
            )
        )
    if "sns_destination" in value:
        import capo_pinpoint_sms_voice.types.sns_destination

        out["SnsDestination"] = (
            capo_pinpoint_sms_voice.types.sns_destination.serialize_json(
                value["sns_destination"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventDestinationDefinition:
    out: EventDestinationDefinition = {}  # type: ignore[typeddict-item]
    if "CloudWatchLogsDestination" in data:
        import capo_pinpoint_sms_voice.types.cloud_watch_logs_destination

        out["cloud_watch_logs_destination"] = (
            capo_pinpoint_sms_voice.types.cloud_watch_logs_destination.deserialize_json(
                data["CloudWatchLogsDestination"]
            )
        )
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "KinesisFirehoseDestination" in data:
        import capo_pinpoint_sms_voice.types.kinesis_firehose_destination

        out["kinesis_firehose_destination"] = (
            capo_pinpoint_sms_voice.types.kinesis_firehose_destination.deserialize_json(
                data["KinesisFirehoseDestination"]
            )
        )
    if "MatchingEventTypes" in data:
        import capo_pinpoint_sms_voice.types.event_types

        out["matching_event_types"] = (
            capo_pinpoint_sms_voice.types.event_types.deserialize_json(
                data["MatchingEventTypes"]
            )
        )
    if "SnsDestination" in data:
        import capo_pinpoint_sms_voice.types.sns_destination

        out["sns_destination"] = (
            capo_pinpoint_sms_voice.types.sns_destination.deserialize_json(
                data["SnsDestination"]
            )
        )
    return out
