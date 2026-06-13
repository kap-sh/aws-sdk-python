"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#UpdateEventDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn
    import aws_sdk_pinpoint_sms_voice_v2.types.event_destination_name
    import aws_sdk_pinpoint_sms_voice_v2.types.event_type_list
    import aws_sdk_pinpoint_sms_voice_v2.types.kinesis_firehose_destination
    import aws_sdk_pinpoint_sms_voice_v2.types.sns_destination


class UpdateEventDestinationRequest(TypedDict):
    configuration_set_name: "aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
    """<p>The configuration set to update with the new event destination. Valid values for this can be the ConfigurationSetName or ConfigurationSetArn.</p>"""
    event_destination_name: "aws_sdk_pinpoint_sms_voice_v2.types.event_destination_name.EventDestinationName"
    """<p>The name to use for the event destination.</p>"""
    enabled: NotRequired["bool"]
    """<p>When set to true logging is enabled.</p>"""
    matching_event_types: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.event_type_list.EventTypeList"
    ]
    """<p>An array of event types that determine which events to log.</p> <note> <p>The <code>TEXT_SENT</code> event type is not supported.</p> </note>"""
    cloud_watch_logs_destination: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.cloud_watch_logs_destination.CloudWatchLogsDestination"
    ]
    """<p>An object that contains information about an event destination that sends data to CloudWatch Logs.</p>"""
    kinesis_firehose_destination: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.kinesis_firehose_destination.KinesisFirehoseDestination"
    ]
    """<p>An object that contains information about an event destination for logging to Firehose.</p>"""
    sns_destination: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.sns_destination.SnsDestination"
    ]
    """<p>An object that contains information about an event destination that sends data to Amazon SNS.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEventDestinationRequest) -> dict:
    out: dict = {}
    out["ConfigurationSetName"] = value["configuration_set_name"]
    out["EventDestinationName"] = value["event_destination_name"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "matching_event_types" in value:
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


def deserialize_aws_json_1_0(data: dict) -> UpdateEventDestinationRequest:
    out: UpdateEventDestinationRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    else:
        raise DeserializationError(
            "UpdateEventDestinationRequest.configuration_set_name required"
        )
    if "EventDestinationName" in data:
        out["event_destination_name"] = data["EventDestinationName"]
    else:
        raise DeserializationError(
            "UpdateEventDestinationRequest.event_destination_name required"
        )
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "MatchingEventTypes" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.event_type_list

        out["matching_event_types"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.event_type_list.deserialize_aws_json_1_0(
                data["MatchingEventTypes"]
            )
        )
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
