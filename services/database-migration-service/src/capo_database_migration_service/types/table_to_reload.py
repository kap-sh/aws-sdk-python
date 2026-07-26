"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TableToReload``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class TableToReload(TypedDict, closed=True):
    schema_name: "capo_database_migration_service.types.string.String"
    """<p>The schema name of the table to be reloaded.</p>"""
    table_name: "capo_database_migration_service.types.string.String"
    """<p>The table name of the table to be reloaded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableToReload) -> dict:
    out: dict = {}
    out["SchemaName"] = value["schema_name"]
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TableToReload:
    out: TableToReload = {}  # type: ignore[typeddict-item]
    if "SchemaName" in data:
        out["schema_name"] = data["SchemaName"]
    else:
        raise DeserializationError("TableToReload.schema_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("TableToReload.table_name required")
    return out
