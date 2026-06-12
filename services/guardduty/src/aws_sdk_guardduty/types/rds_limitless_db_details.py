"""Generated from Smithy shape ``com.amazonaws.guardduty#RdsLimitlessDbDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.tags


class RdsLimitlessDbDetails(TypedDict):
    db_shard_group_identifier: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name associated with the Limitless DB shard group.</p>"""
    db_shard_group_resource_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The resource identifier of the DB shard group within the Limitless Database.</p>"""
    db_shard_group_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies the DB shard group.</p>"""
    engine: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The database engine of the database instance involved in the finding.</p>"""
    engine_version: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The version of the database engine.</p>"""
    db_cluster_identifier: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the database cluster that is a part of the Limitless Database.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tags.Tags"]
    """<p>Information about the tag key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsLimitlessDbDetails) -> dict:
    out: dict = {}
    if "db_shard_group_identifier" in value:
        out["dbShardGroupIdentifier"] = value["db_shard_group_identifier"]
    if "db_shard_group_resource_id" in value:
        out["dbShardGroupResourceId"] = value["db_shard_group_resource_id"]
    if "db_shard_group_arn" in value:
        out["dbShardGroupArn"] = value["db_shard_group_arn"]
    if "engine" in value:
        out["engine"] = value["engine"]
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "db_cluster_identifier" in value:
        out["dbClusterIdentifier"] = value["db_cluster_identifier"]
    if "tags" in value:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RdsLimitlessDbDetails:
    out: RdsLimitlessDbDetails = {}  # type: ignore[typeddict-item]
    if "dbShardGroupIdentifier" in data:
        out["db_shard_group_identifier"] = data["dbShardGroupIdentifier"]
    if "dbShardGroupResourceId" in data:
        out["db_shard_group_resource_id"] = data["dbShardGroupResourceId"]
    if "dbShardGroupArn" in data:
        out["db_shard_group_arn"] = data["dbShardGroupArn"]
    if "engine" in data:
        out["engine"] = data["engine"]
    if "engineVersion" in data:
        out["engine_version"] = data["engineVersion"]
    if "dbClusterIdentifier" in data:
        out["db_cluster_identifier"] = data["dbClusterIdentifier"]
    if "tags" in data:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.deserialize_json(data["tags"])
    return out
