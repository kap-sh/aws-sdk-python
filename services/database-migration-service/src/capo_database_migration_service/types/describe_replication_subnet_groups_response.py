"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationSubnetGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication_subnet_groups
    import capo_database_migration_service.types.string


class DescribeReplicationSubnetGroupsResponse(TypedDict, closed=True):
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    replication_subnet_groups: NotRequired[
        "capo_database_migration_service.types.replication_subnet_groups.ReplicationSubnetGroups"
    ]
    """<p>A description of the replication subnet groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplicationSubnetGroupsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "replication_subnet_groups" in value:
        import capo_database_migration_service.types.replication_subnet_groups

        out["ReplicationSubnetGroups"] = (
            capo_database_migration_service.types.replication_subnet_groups.serialize_aws_json_1_1(
                value["replication_subnet_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplicationSubnetGroupsResponse:
    out: DescribeReplicationSubnetGroupsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "ReplicationSubnetGroups" in data:
        import capo_database_migration_service.types.replication_subnet_groups

        out["replication_subnet_groups"] = (
            capo_database_migration_service.types.replication_subnet_groups.deserialize_aws_json_1_1(
                data["ReplicationSubnetGroups"]
            )
        )
    return out
