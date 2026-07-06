"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeSnapshotScheduleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.description
    import aws_sdk_storage_gateway.types.gateway_timezone
    import aws_sdk_storage_gateway.types.hour_of_day
    import aws_sdk_storage_gateway.types.recurrence_in_hours
    import aws_sdk_storage_gateway.types.tags
    import aws_sdk_storage_gateway.types.volume_arn


class DescribeSnapshotScheduleOutput(TypedDict, closed=True):
    volume_arn: NotRequired["aws_sdk_storage_gateway.types.volume_arn.VolumeARN"]
    """<p>The Amazon Resource Name (ARN) of the volume that was specified in the request.</p>"""
    start_at: NotRequired["aws_sdk_storage_gateway.types.hour_of_day.HourOfDay"]
    """<p>The hour of the day at which the snapshot schedule begins represented as <i>hh</i>, where <i>hh</i> is the hour (0 to 23). The hour of the day is in the time zone of the gateway.</p>"""
    recurrence_in_hours: NotRequired[
        "aws_sdk_storage_gateway.types.recurrence_in_hours.RecurrenceInHours"
    ]
    """<p>The number of hours between snapshots.</p>"""
    description: NotRequired["aws_sdk_storage_gateway.types.description.Description"]
    """<p>The snapshot description.</p>"""
    timezone: NotRequired[
        "aws_sdk_storage_gateway.types.gateway_timezone.GatewayTimezone"
    ]
    """<p>A value that indicates the time zone of the gateway.</p>"""
    tags: NotRequired["aws_sdk_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags assigned to the snapshot schedule, sorted alphabetically by key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags using the <code>ListTagsForResource</code> API operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSnapshotScheduleOutput) -> dict:
    out: dict = {}
    if "volume_arn" in value:
        out["VolumeARN"] = value["volume_arn"]
    if "start_at" in value:
        out["StartAt"] = value["start_at"]
    if "recurrence_in_hours" in value:
        out["RecurrenceInHours"] = value["recurrence_in_hours"]
    if "description" in value:
        out["Description"] = value["description"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    if "tags" in value:
        import aws_sdk_storage_gateway.types.tags

        out["Tags"] = aws_sdk_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSnapshotScheduleOutput:
    out: DescribeSnapshotScheduleOutput = {}  # type: ignore[typeddict-item]
    if "VolumeARN" in data:
        out["volume_arn"] = data["VolumeARN"]
    if "StartAt" in data:
        out["start_at"] = data["StartAt"]
    if "RecurrenceInHours" in data:
        out["recurrence_in_hours"] = data["RecurrenceInHours"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Timezone" in data:
        out["timezone"] = data["Timezone"]
    if "Tags" in data:
        import aws_sdk_storage_gateway.types.tags

        out["tags"] = aws_sdk_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
