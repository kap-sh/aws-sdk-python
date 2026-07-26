"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication_instance_list
    import capo_database_migration_service.types.string


class DescribeReplicationInstancesResponse(TypedDict, closed=True):
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    replication_instances: NotRequired[
        "capo_database_migration_service.types.replication_instance_list.ReplicationInstanceList"
    ]
    """<p>The replication instances described.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplicationInstancesResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "replication_instances" in value:
        import capo_database_migration_service.types.replication_instance_list

        out["ReplicationInstances"] = (
            capo_database_migration_service.types.replication_instance_list.serialize_aws_json_1_1(
                value["replication_instances"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplicationInstancesResponse:
    out: DescribeReplicationInstancesResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "ReplicationInstances" in data:
        import capo_database_migration_service.types.replication_instance_list

        out["replication_instances"] = (
            capo_database_migration_service.types.replication_instance_list.deserialize_aws_json_1_1(
                data["ReplicationInstances"]
            )
        )
    return out
