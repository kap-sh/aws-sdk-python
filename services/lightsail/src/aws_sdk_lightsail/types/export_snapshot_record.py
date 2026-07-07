"""Generated from Smithy shape ``com.amazonaws.lightsail#ExportSnapshotRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.destination_info
    import aws_sdk_lightsail.types.export_snapshot_record_source_info
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.record_state
    import aws_sdk_lightsail.types.resource_location
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.resource_type


class ExportSnapshotRecord(TypedDict, closed=True):
    name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The export snapshot record name.</p>"""
    arn: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the export snapshot record.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The date when the export snapshot record was created.</p>"""
    location: NotRequired["aws_sdk_lightsail.types.resource_location.ResourceLocation"]
    """<p>The AWS Region and Availability Zone where the export snapshot record is located.</p>"""
    resource_type: NotRequired["aws_sdk_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type (<code>ExportSnapshotRecord</code>).</p>"""
    state: NotRequired["aws_sdk_lightsail.types.record_state.RecordState"]
    """<p>The state of the export snapshot record.</p>"""
    source_info: NotRequired[
        "aws_sdk_lightsail.types.export_snapshot_record_source_info.ExportSnapshotRecordSourceInfo"
    ]
    """<p>A list of objects describing the source of the export snapshot record.</p>"""
    destination_info: NotRequired[
        "aws_sdk_lightsail.types.destination_info.DestinationInfo"
    ]
    """<p>A list of objects describing the destination of the export snapshot record.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportSnapshotRecord) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.serialize_aws_json_1_1(
                value["location"]
            )
        )
    if "resource_type" in value:
        import aws_sdk_lightsail.types.resource_type

        out["resourceType"] = (
            aws_sdk_lightsail.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "state" in value:
        import aws_sdk_lightsail.types.record_state

        out["state"] = aws_sdk_lightsail.types.record_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "source_info" in value:
        import aws_sdk_lightsail.types.export_snapshot_record_source_info

        out["sourceInfo"] = (
            aws_sdk_lightsail.types.export_snapshot_record_source_info.serialize_aws_json_1_1(
                value["source_info"]
            )
        )
    if "destination_info" in value:
        import aws_sdk_lightsail.types.destination_info

        out["destinationInfo"] = (
            aws_sdk_lightsail.types.destination_info.serialize_aws_json_1_1(
                value["destination_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportSnapshotRecord:
    out: ExportSnapshotRecord = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "location" in data:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if "resourceType" in data:
        import aws_sdk_lightsail.types.resource_type

        out["resource_type"] = (
            aws_sdk_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "state" in data:
        import aws_sdk_lightsail.types.record_state

        out["state"] = aws_sdk_lightsail.types.record_state.deserialize_aws_json_1_1(
            data["state"]
        )
    if "sourceInfo" in data:
        import aws_sdk_lightsail.types.export_snapshot_record_source_info

        out["source_info"] = (
            aws_sdk_lightsail.types.export_snapshot_record_source_info.deserialize_aws_json_1_1(
                data["sourceInfo"]
            )
        )
    if "destinationInfo" in data:
        import aws_sdk_lightsail.types.destination_info

        out["destination_info"] = (
            aws_sdk_lightsail.types.destination_info.deserialize_aws_json_1_1(
                data["destinationInfo"]
            )
        )
    return out
