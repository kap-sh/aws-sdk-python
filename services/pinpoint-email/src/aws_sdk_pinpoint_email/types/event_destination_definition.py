"""Generated from Smithy shape ``com.amazonaws.pinpointemail#EventDestinationDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.cloud_watch_destination
    import aws_sdk_pinpoint_email.types.enabled
    import aws_sdk_pinpoint_email.types.event_types
    import aws_sdk_pinpoint_email.types.kinesis_firehose_destination
    import aws_sdk_pinpoint_email.types.pinpoint_destination
    import aws_sdk_pinpoint_email.types.sns_destination


class EventDestinationDefinition(TypedDict):
    enabled: "aws_sdk_pinpoint_email.types.enabled.Enabled"
    """<p>If <code>true</code>, the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this <code>EventDestinationDefinition</code>.</p> <p>If <code>false</code>, the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.</p>"""
    matching_event_types: NotRequired[
        "aws_sdk_pinpoint_email.types.event_types.EventTypes"
    ]
    """<p>An array that specifies which events Amazon Pinpoint should send to the destinations in this <code>EventDestinationDefinition</code>.</p>"""
    kinesis_firehose_destination: NotRequired[
        "aws_sdk_pinpoint_email.types.kinesis_firehose_destination.KinesisFirehoseDestination"
    ]
    """<p>An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.</p>"""
    cloud_watch_destination: NotRequired[
        "aws_sdk_pinpoint_email.types.cloud_watch_destination.CloudWatchDestination"
    ]
    """<p>An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.</p>"""
    sns_destination: NotRequired[
        "aws_sdk_pinpoint_email.types.sns_destination.SnsDestination"
    ]
    """<p>An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notification when certain email events occur.</p>"""
    pinpoint_destination: NotRequired[
        "aws_sdk_pinpoint_email.types.pinpoint_destination.PinpointDestination"
    ]
    """<p>An object that defines a Amazon Pinpoint destination for email events. You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventDestinationDefinition) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    if "matching_event_types" in value:
        import aws_sdk_pinpoint_email.types.event_types

        out["MatchingEventTypes"] = (
            aws_sdk_pinpoint_email.types.event_types.serialize_json(
                value["matching_event_types"]
            )
        )
    if "kinesis_firehose_destination" in value:
        import aws_sdk_pinpoint_email.types.kinesis_firehose_destination

        out["KinesisFirehoseDestination"] = (
            aws_sdk_pinpoint_email.types.kinesis_firehose_destination.serialize_json(
                value["kinesis_firehose_destination"]
            )
        )
    if "cloud_watch_destination" in value:
        import aws_sdk_pinpoint_email.types.cloud_watch_destination

        out["CloudWatchDestination"] = (
            aws_sdk_pinpoint_email.types.cloud_watch_destination.serialize_json(
                value["cloud_watch_destination"]
            )
        )
    if "sns_destination" in value:
        import aws_sdk_pinpoint_email.types.sns_destination

        out["SnsDestination"] = (
            aws_sdk_pinpoint_email.types.sns_destination.serialize_json(
                value["sns_destination"]
            )
        )
    if "pinpoint_destination" in value:
        import aws_sdk_pinpoint_email.types.pinpoint_destination

        out["PinpointDestination"] = (
            aws_sdk_pinpoint_email.types.pinpoint_destination.serialize_json(
                value["pinpoint_destination"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventDestinationDefinition:
    out: EventDestinationDefinition = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if "MatchingEventTypes" in data:
        import aws_sdk_pinpoint_email.types.event_types

        out["matching_event_types"] = (
            aws_sdk_pinpoint_email.types.event_types.deserialize_json(
                data["MatchingEventTypes"]
            )
        )
    if "KinesisFirehoseDestination" in data:
        import aws_sdk_pinpoint_email.types.kinesis_firehose_destination

        out["kinesis_firehose_destination"] = (
            aws_sdk_pinpoint_email.types.kinesis_firehose_destination.deserialize_json(
                data["KinesisFirehoseDestination"]
            )
        )
    if "CloudWatchDestination" in data:
        import aws_sdk_pinpoint_email.types.cloud_watch_destination

        out["cloud_watch_destination"] = (
            aws_sdk_pinpoint_email.types.cloud_watch_destination.deserialize_json(
                data["CloudWatchDestination"]
            )
        )
    if "SnsDestination" in data:
        import aws_sdk_pinpoint_email.types.sns_destination

        out["sns_destination"] = (
            aws_sdk_pinpoint_email.types.sns_destination.deserialize_json(
                data["SnsDestination"]
            )
        )
    if "PinpointDestination" in data:
        import aws_sdk_pinpoint_email.types.pinpoint_destination

        out["pinpoint_destination"] = (
            aws_sdk_pinpoint_email.types.pinpoint_destination.deserialize_json(
                data["PinpointDestination"]
            )
        )
    return out
