"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribePendingMaintenanceActionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.filter_list
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.string


class DescribePendingMaintenanceActionsMessage(TypedDict):
    replication_instance_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the replication instance.</p>"""
    filters: NotRequired[
        "aws_sdk_database_migration_service.types.filter_list.FilterList"
    ]
    """<p></p>"""
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    max_records: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePendingMaintenanceActionsMessage) -> dict:
    out: dict = {}
    if "replication_instance_arn" in value:
        out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    if "filters" in value:
        import aws_sdk_database_migration_service.types.filter_list

        out["Filters"] = (
            aws_sdk_database_migration_service.types.filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePendingMaintenanceActionsMessage:
    out: DescribePendingMaintenanceActionsMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationInstanceArn" in data:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    if "Filters" in data:
        import aws_sdk_database_migration_service.types.filter_list

        out["filters"] = (
            aws_sdk_database_migration_service.types.filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    return out
