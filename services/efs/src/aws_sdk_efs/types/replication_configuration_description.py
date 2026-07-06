"""Generated from Smithy shape ``com.amazonaws.efs#ReplicationConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_efs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_efs.types.aws_account_id
    import aws_sdk_efs.types.destinations
    import aws_sdk_efs.types.file_system_arn
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.region_name
    import aws_sdk_efs.types.timestamp


class ReplicationConfigurationDescription(TypedDict, closed=True):
    source_file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the source Amazon EFS file system that is being replicated.</p>"""
    source_file_system_region: "aws_sdk_efs.types.region_name.RegionName"
    """<p>The Amazon Web Services Region in which the source EFS file system is located.</p>"""
    source_file_system_arn: "aws_sdk_efs.types.file_system_arn.FileSystemArn"
    """<p>The Amazon Resource Name (ARN) of the current source file system in the replication configuration.</p>"""
    original_source_file_system_arn: "aws_sdk_efs.types.file_system_arn.FileSystemArn"
    """<p>The Amazon Resource Name (ARN) of the original source EFS file system in the replication configuration.</p>"""
    creation_time: "aws_sdk_efs.types.timestamp.Timestamp"
    """<p>Describes when the replication configuration was created.</p>"""
    destinations: "aws_sdk_efs.types.destinations.Destinations"
    """<p>An array of destination objects. Only one destination object is supported.</p>"""
    source_file_system_owner_id: NotRequired[
        "aws_sdk_efs.types.aws_account_id.AwsAccountId"
    ]
    """<p>ID of the Amazon Web Services account in which the source file system resides.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationConfigurationDescription) -> dict:
    out: dict = {}
    out["SourceFileSystemId"] = value["source_file_system_id"]
    out["SourceFileSystemRegion"] = value["source_file_system_region"]
    out["SourceFileSystemArn"] = value["source_file_system_arn"]
    out["OriginalSourceFileSystemArn"] = value["original_source_file_system_arn"]
    import aws_sdk_efs.types.timestamp

    out["CreationTime"] = aws_sdk_efs.types.timestamp.serialize_json(
        value["creation_time"]
    )
    import aws_sdk_efs.types.destinations

    out["Destinations"] = aws_sdk_efs.types.destinations.serialize_json(
        value["destinations"]
    )
    if "source_file_system_owner_id" in value:
        out["SourceFileSystemOwnerId"] = value["source_file_system_owner_id"]
    return out


def deserialize_json(data: dict) -> ReplicationConfigurationDescription:
    out: ReplicationConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "SourceFileSystemId" in data:
        out["source_file_system_id"] = data["SourceFileSystemId"]
    else:
        raise DeserializationError(
            "ReplicationConfigurationDescription.source_file_system_id required"
        )
    if "SourceFileSystemRegion" in data:
        out["source_file_system_region"] = data["SourceFileSystemRegion"]
    else:
        raise DeserializationError(
            "ReplicationConfigurationDescription.source_file_system_region required"
        )
    if "SourceFileSystemArn" in data:
        out["source_file_system_arn"] = data["SourceFileSystemArn"]
    else:
        raise DeserializationError(
            "ReplicationConfigurationDescription.source_file_system_arn required"
        )
    if "OriginalSourceFileSystemArn" in data:
        out["original_source_file_system_arn"] = data["OriginalSourceFileSystemArn"]
    else:
        raise DeserializationError(
            "ReplicationConfigurationDescription.original_source_file_system_arn required"
        )
    if "CreationTime" in data:
        import aws_sdk_efs.types.timestamp

        out["creation_time"] = aws_sdk_efs.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    else:
        raise DeserializationError(
            "ReplicationConfigurationDescription.creation_time required"
        )
    if "Destinations" in data:
        import aws_sdk_efs.types.destinations

        out["destinations"] = aws_sdk_efs.types.destinations.deserialize_json(
            data["Destinations"]
        )
    else:
        raise DeserializationError(
            "ReplicationConfigurationDescription.destinations required"
        )
    if "SourceFileSystemOwnerId" in data:
        out["source_file_system_owner_id"] = data["SourceFileSystemOwnerId"]
    return out
