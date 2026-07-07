"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#EventDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination
    import aws_sdk_pinpoint_sms_voice_v2.types.event_destination_name
    import aws_sdk_pinpoint_sms_voice_v2.types.event_type_list
    import aws_sdk_pinpoint_sms_voice_v2.types.kinesis_firehose_destination
    import aws_sdk_pinpoint_sms_voice_v2.types.sns_destination


class EventDestination(TypedDict, closed=True):
    event_destination_name: "aws_sdk_pinpoint_sms_voice_v2.types.event_destination_name.EventDestinationName"
    """<p>The name of the EventDestination.</p>"""
    enabled: "bool"
    """<p>When set to true events will be logged.</p>"""
    matching_event_types: (
        "aws_sdk_pinpoint_sms_voice_v2.types.event_type_list.EventTypeList"
    )
    """<p>An array of event types that determine which events to log.</p> <note> <p>The <code>TEXT_SENT</code> event type is not supported.</p> </note>"""
    cloud_watch_logs_destination: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination.CloudWatchLogsDestination"
    ]
    """<p>An object that contains information about an event destination that sends logging events to Amazon CloudWatch logs.</p>"""
    kinesis_firehose_destination: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.kinesis_firehose_destination.KinesisFirehoseDestination"
    ]
    """<p>An object that contains information about an event destination for logging to Amazon Data Firehose.</p>"""
    sns_destination: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.sns_destination.SnsDestination"
    ]
    """<p>An object that contains information about an event destination that sends logging events to Amazon SNS.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventDestination) -> dict:
    out: dict = {}
    out["EventDestinationName"] = value["event_destination_name"]
    out["Enabled"] = value["enabled"]
    import aws_sdk_pinpoint_sms_voice_v2.types.event_type_list

    out["MatchingEventTypes"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.event_type_list.serialize_aws_json_1_0(
            value["matching_event_types"]
        )
    )
    if "cloud_watch_logs_destination" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination

        out["CloudWatchLogsDestination"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination.serialize_aws_json_1_0(
                value["cloud_watch_logs_destination"]
            )
        )
    if "kinesis_firehose_destination" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.kinesis_firehose_destination

        out["KinesisFirehoseDestination"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.kinesis_firehose_destination.serialize_aws_json_1_0(
                value["kinesis_firehose_destination"]
            )
        )
    if "sns_destination" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.sns_destination

        out["SnsDestination"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.sns_destination.serialize_aws_json_1_0(
                value["sns_destination"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EventDestination:
    out: EventDestination = {}  # type: ignore[typeddict-item]
    if "EventDestinationName" in data:
        out["event_destination_name"] = data["EventDestinationName"]
    else:
        raise DeserializationError("EventDestination.event_destination_name required")
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("EventDestination.enabled required")
    if "MatchingEventTypes" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.event_type_list

        out["matching_event_types"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.event_type_list.deserialize_aws_json_1_0(
                data["MatchingEventTypes"]
            )
        )
    else:
        raise DeserializationError("EventDestination.matching_event_types required")
    if "CloudWatchLogsDestination" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination

        out["cloud_watch_logs_destination"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination.deserialize_aws_json_1_0(
                data["CloudWatchLogsDestination"]
            )
        )
    if "KinesisFirehoseDestination" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.kinesis_firehose_destination

        out["kinesis_firehose_destination"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.kinesis_firehose_destination.deserialize_aws_json_1_0(
                data["KinesisFirehoseDestination"]
            )
        )
    if "SnsDestination" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.sns_destination

        out["sns_destination"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.sns_destination.deserialize_aws_json_1_0(
                data["SnsDestination"]
            )
        )
    return out
