"""Generated from Smithy shape ``com.amazonaws.s3#QueueConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.event_list
    import aws_sdk_s3.types.notification_configuration_filter
    import aws_sdk_s3.types.notification_id
    import aws_sdk_s3.types.queue_arn


class QueueConfiguration(TypedDict):
    id: NotRequired["aws_sdk_s3.types.notification_id.NotificationId"]
    queue_arn: "aws_sdk_s3.types.queue_arn.QueueArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message when it detects events of the specified type.</p>"""
    events: "aws_sdk_s3.types.event_list.EventList"
    """<p>A collection of bucket events for which to send notifications</p>"""
    filter: NotRequired[
        "aws_sdk_s3.types.notification_configuration_filter.NotificationConfigurationFilter"
    ]


# --- restXml ser/de ---
def serialize_xml(value: QueueConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Queue").text = str(value["queue_arn"])
    import aws_sdk_s3.types.event_list

    aws_sdk_s3.types.event_list.serialize_xml_flat(value["events"], el, "Event")
    if "filter" in value:
        import aws_sdk_s3.types.notification_configuration_filter

        aws_sdk_s3.types.notification_configuration_filter.serialize_xml(
            value["filter"], el, "Filter"
        )


def deserialize_xml(el: Element) -> QueueConfiguration:
    out: QueueConfiguration = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_queue_arn = el.find("Queue")
    if child_queue_arn is not None:
        out["queue_arn"] = str(child_queue_arn.text or "")
    else:
        raise DeserializationError("QueueConfiguration.queue_arn required")
    if el.find("Event") is not None:
        import aws_sdk_s3.types.event_list

        out["events"] = aws_sdk_s3.types.event_list.deserialize_xml_flat(el, "Event")
    else:
        raise DeserializationError("QueueConfiguration.events required")
    child_filter = el.find("Filter")
    if child_filter is not None:
        import aws_sdk_s3.types.notification_configuration_filter

        out["filter"] = (
            aws_sdk_s3.types.notification_configuration_filter.deserialize_xml(
                child_filter
            )
        )
    return out
