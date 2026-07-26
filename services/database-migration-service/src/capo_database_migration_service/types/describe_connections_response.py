"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.connection_list
    import capo_database_migration_service.types.string


class DescribeConnectionsResponse(TypedDict, closed=True):
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    connections: NotRequired[
        "capo_database_migration_service.types.connection_list.ConnectionList"
    ]
    """<p>A description of the connections.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "connections" in value:
        import capo_database_migration_service.types.connection_list

        out["Connections"] = (
            capo_database_migration_service.types.connection_list.serialize_aws_json_1_1(
                value["connections"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionsResponse:
    out: DescribeConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Connections" in data:
        import capo_database_migration_service.types.connection_list

        out["connections"] = (
            capo_database_migration_service.types.connection_list.deserialize_aws_json_1_1(
                data["Connections"]
            )
        )
    return out
