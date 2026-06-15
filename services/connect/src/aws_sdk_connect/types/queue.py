"""Generated from Smithy shape ``com.amazonaws.connect#Queue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.common_name_length127
    import aws_sdk_connect.types.hours_of_operation_id
    import aws_sdk_connect.types.outbound_caller_config
    import aws_sdk_connect.types.outbound_email_config
    import aws_sdk_connect.types.queue_description
    import aws_sdk_connect.types.queue_id
    import aws_sdk_connect.types.queue_max_contacts
    import aws_sdk_connect.types.queue_status
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp


class Queue(TypedDict):
    name: NotRequired["aws_sdk_connect.types.common_name_length127.CommonNameLength127"]
    """<p>The name of the queue.</p>"""
    queue_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the queue.</p>"""
    queue_id: NotRequired["aws_sdk_connect.types.queue_id.QueueId"]
    """<p>The identifier for the queue.</p>"""
    description: NotRequired["aws_sdk_connect.types.queue_description.QueueDescription"]
    """<p>The description of the queue.</p>"""
    outbound_caller_config: NotRequired[
        "aws_sdk_connect.types.outbound_caller_config.OutboundCallerConfig"
    ]
    """<p>The outbound caller ID name, number, and outbound whisper flow.</p>"""
    outbound_email_config: NotRequired[
        "aws_sdk_connect.types.outbound_email_config.OutboundEmailConfig"
    ]
    """<p>The outbound email address ID for a specified queue.</p>"""
    hours_of_operation_id: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_id.HoursOfOperationId"
    ]
    """<p>The identifier for the hours of operation.</p>"""
    max_contacts: NotRequired[
        "aws_sdk_connect.types.queue_max_contacts.QueueMaxContacts"
    ]
    """<p>The maximum number of contacts that can be in the queue before it is considered full.</p>"""
    status: NotRequired["aws_sdk_connect.types.queue_status.QueueStatus"]
    """<p>The status of the queue.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Queue) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "queue_arn" in value:
        out["QueueArn"] = value["queue_arn"]
    if "queue_id" in value:
        out["QueueId"] = value["queue_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "outbound_caller_config" in value:
        import aws_sdk_connect.types.outbound_caller_config

        out["OutboundCallerConfig"] = (
            aws_sdk_connect.types.outbound_caller_config.serialize_json(
                value["outbound_caller_config"]
            )
        )
    if "outbound_email_config" in value:
        import aws_sdk_connect.types.outbound_email_config

        out["OutboundEmailConfig"] = (
            aws_sdk_connect.types.outbound_email_config.serialize_json(
                value["outbound_email_config"]
            )
        )
    if "hours_of_operation_id" in value:
        out["HoursOfOperationId"] = value["hours_of_operation_id"]
    if "max_contacts" in value:
        out["MaxContacts"] = value["max_contacts"]
    if "status" in value:
        import aws_sdk_connect.types.queue_status

        out["Status"] = aws_sdk_connect.types.queue_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> Queue:
    out: Queue = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "QueueArn" in data:
        out["queue_arn"] = data["QueueArn"]
    if "QueueId" in data:
        out["queue_id"] = data["QueueId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "OutboundCallerConfig" in data:
        import aws_sdk_connect.types.outbound_caller_config

        out["outbound_caller_config"] = (
            aws_sdk_connect.types.outbound_caller_config.deserialize_json(
                data["OutboundCallerConfig"]
            )
        )
    if "OutboundEmailConfig" in data:
        import aws_sdk_connect.types.outbound_email_config

        out["outbound_email_config"] = (
            aws_sdk_connect.types.outbound_email_config.deserialize_json(
                data["OutboundEmailConfig"]
            )
        )
    if "HoursOfOperationId" in data:
        out["hours_of_operation_id"] = data["HoursOfOperationId"]
    if "MaxContacts" in data:
        out["max_contacts"] = data["MaxContacts"]
    if "Status" in data:
        import aws_sdk_connect.types.queue_status

        out["status"] = aws_sdk_connect.types.queue_status.deserialize_json(
            data["Status"]
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
