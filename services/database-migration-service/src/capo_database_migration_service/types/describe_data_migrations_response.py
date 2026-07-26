"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeDataMigrationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.data_migrations
    import capo_database_migration_service.types.marker


class DescribeDataMigrationsResponse(TypedDict, closed=True):
    data_migrations: NotRequired[
        "capo_database_migration_service.types.data_migrations.DataMigrations"
    ]
    """<p>Returns information about the data migrations used in the project.</p>"""
    marker: NotRequired["capo_database_migration_service.types.marker.Marker"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataMigrationsResponse) -> dict:
    out: dict = {}
    if "data_migrations" in value:
        import capo_database_migration_service.types.data_migrations

        out["DataMigrations"] = (
            capo_database_migration_service.types.data_migrations.serialize_aws_json_1_1(
                value["data_migrations"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDataMigrationsResponse:
    out: DescribeDataMigrationsResponse = {}  # type: ignore[typeddict-item]
    if "DataMigrations" in data:
        import capo_database_migration_service.types.data_migrations

        out["data_migrations"] = (
            capo_database_migration_service.types.data_migrations.deserialize_aws_json_1_1(
                data["DataMigrations"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
