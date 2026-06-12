"""Generated from Smithy shape ``com.amazonaws.guardduty#RdsDbInstanceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.tags


class RdsDbInstanceDetails(TypedDict):
    db_instance_identifier: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The identifier associated to the database instance that was involved in the finding.</p>"""
    engine: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The database engine of the database instance involved in the finding.</p>"""
    engine_version: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The version of the database engine that was involved in the finding.</p>"""
    db_cluster_identifier: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The identifier of the database cluster that contains the database instance ID involved in the finding.</p>"""
    db_instance_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies the database instance involved in the finding.</p>"""
    dbi_resource_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The unique ID of the database resource involved in the activity that prompted GuardDuty to generate the finding.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tags.Tags"]
    """<p>Information about the tag key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsDbInstanceDetails) -> dict:
    out: dict = {}
    if "db_instance_identifier" in value:
        out["dbInstanceIdentifier"] = value["db_instance_identifier"]
    if "engine" in value:
        out["engine"] = value["engine"]
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "db_cluster_identifier" in value:
        out["dbClusterIdentifier"] = value["db_cluster_identifier"]
    if "db_instance_arn" in value:
        out["dbInstanceArn"] = value["db_instance_arn"]
    if "dbi_resource_id" in value:
        out["dbiResourceId"] = value["dbi_resource_id"]
    if "tags" in value:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RdsDbInstanceDetails:
    out: RdsDbInstanceDetails = {}  # type: ignore[typeddict-item]
    if "dbInstanceIdentifier" in data:
        out["db_instance_identifier"] = data["dbInstanceIdentifier"]
    if "engine" in data:
        out["engine"] = data["engine"]
    if "engineVersion" in data:
        out["engine_version"] = data["engineVersion"]
    if "dbClusterIdentifier" in data:
        out["db_cluster_identifier"] = data["dbClusterIdentifier"]
    if "dbInstanceArn" in data:
        out["db_instance_arn"] = data["dbInstanceArn"]
    if "dbiResourceId" in data:
        out["dbi_resource_id"] = data["dbiResourceId"]
    if "tags" in data:
        import aws_sdk_guardduty.types.tags

        out["tags"] = aws_sdk_guardduty.types.tags.deserialize_json(data["tags"])
    return out
