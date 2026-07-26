"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeSchemasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.schema_list
    import capo_database_migration_service.types.string


class DescribeSchemasResponse(TypedDict, closed=True):
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    schemas: NotRequired["capo_database_migration_service.types.schema_list.SchemaList"]
    """<p>The described schema.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSchemasResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "schemas" in value:
        import capo_database_migration_service.types.schema_list

        out["Schemas"] = (
            capo_database_migration_service.types.schema_list.serialize_aws_json_1_1(
                value["schemas"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSchemasResponse:
    out: DescribeSchemasResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Schemas" in data:
        import capo_database_migration_service.types.schema_list

        out["schemas"] = (
            capo_database_migration_service.types.schema_list.deserialize_aws_json_1_1(
                data["Schemas"]
            )
        )
    return out
