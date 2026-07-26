"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeOrderableReplicationInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.orderable_replication_instance_list
    import capo_database_migration_service.types.string


class DescribeOrderableReplicationInstancesResponse(TypedDict, closed=True):
    orderable_replication_instances: NotRequired[
        "capo_database_migration_service.types.orderable_replication_instance_list.OrderableReplicationInstanceList"
    ]
    """<p>The order-able replication instances available.</p>"""
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeOrderableReplicationInstancesResponse,
) -> dict:
    out: dict = {}
    if "orderable_replication_instances" in value:
        import capo_database_migration_service.types.orderable_replication_instance_list

        out["OrderableReplicationInstances"] = (
            capo_database_migration_service.types.orderable_replication_instance_list.serialize_aws_json_1_1(
                value["orderable_replication_instances"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeOrderableReplicationInstancesResponse:
    out: DescribeOrderableReplicationInstancesResponse = {}  # type: ignore[typeddict-item]
    if "OrderableReplicationInstances" in data:
        import capo_database_migration_service.types.orderable_replication_instance_list

        out["orderable_replication_instances"] = (
            capo_database_migration_service.types.orderable_replication_instance_list.deserialize_aws_json_1_1(
                data["OrderableReplicationInstances"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
