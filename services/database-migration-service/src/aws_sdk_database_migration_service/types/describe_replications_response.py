"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_list
    import aws_sdk_database_migration_service.types.string


class DescribeReplicationsResponse(TypedDict):
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    replications: NotRequired[
        "aws_sdk_database_migration_service.types.replication_list.ReplicationList"
    ]
    """<p>The replication descriptions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplicationsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "replications" in value:
        import aws_sdk_database_migration_service.types.replication_list

        out["Replications"] = (
            aws_sdk_database_migration_service.types.replication_list.serialize_aws_json_1_1(
                value["replications"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplicationsResponse:
    out: DescribeReplicationsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Replications" in data:
        import aws_sdk_database_migration_service.types.replication_list

        out["replications"] = (
            aws_sdk_database_migration_service.types.replication_list.deserialize_aws_json_1_1(
                data["Replications"]
            )
        )
    return out
