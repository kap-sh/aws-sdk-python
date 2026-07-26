"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication_config_list
    import capo_database_migration_service.types.string


class DescribeReplicationConfigsResponse(TypedDict, closed=True):
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    replication_configs: NotRequired[
        "capo_database_migration_service.types.replication_config_list.ReplicationConfigList"
    ]
    """<p>Returned configuration parameters that describe each provisioned DMS Serverless replication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplicationConfigsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "replication_configs" in value:
        import capo_database_migration_service.types.replication_config_list

        out["ReplicationConfigs"] = (
            capo_database_migration_service.types.replication_config_list.serialize_aws_json_1_1(
                value["replication_configs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplicationConfigsResponse:
    out: DescribeReplicationConfigsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "ReplicationConfigs" in data:
        import capo_database_migration_service.types.replication_config_list

        out["replication_configs"] = (
            capo_database_migration_service.types.replication_config_list.deserialize_aws_json_1_1(
                data["ReplicationConfigs"]
            )
        )
    return out
