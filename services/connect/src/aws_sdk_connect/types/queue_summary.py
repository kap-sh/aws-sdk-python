"""Generated from Smithy shape ``com.amazonaws.connect#QueueSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.queue_id
    import aws_sdk_connect.types.queue_name
    import aws_sdk_connect.types.queue_type
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.timestamp


class QueueSummary(TypedDict):
    id: NotRequired["aws_sdk_connect.types.queue_id.QueueId"]
    """<p>The identifier of the queue.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the queue.</p>"""
    name: NotRequired["aws_sdk_connect.types.queue_name.QueueName"]
    """<p>The name of the queue.</p>"""
    queue_type: NotRequired["aws_sdk_connect.types.queue_type.QueueType"]
    """<p>The type of queue.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "queue_type" in value:
        import aws_sdk_connect.types.queue_type

        out["QueueType"] = aws_sdk_connect.types.queue_type.serialize_json(
            value["queue_type"]
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> QueueSummary:
    out: QueueSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "QueueType" in data:
        import aws_sdk_connect.types.queue_type

        out["queue_type"] = aws_sdk_connect.types.queue_type.deserialize_json(
            data["QueueType"]
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
