"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetTableOptimizerEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.database_name_string
    import aws_sdk_glue.types.table_name_string
    import aws_sdk_glue.types.table_optimizer_type


class BatchGetTableOptimizerEntry(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The Catalog ID of the table.</p>"""
    database_name: NotRequired[
        "aws_sdk_glue.types.database_name_string.databaseNameString"
    ]
    """<p>The name of the database in the catalog in which the table resides.</p>"""
    table_name: NotRequired["aws_sdk_glue.types.table_name_string.tableNameString"]
    """<p>The name of the table.</p>"""
    type: NotRequired["aws_sdk_glue.types.table_optimizer_type.TableOptimizerType"]
    """<p>The type of table optimizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetTableOptimizerEntry) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["catalogId"] = value["catalog_id"]
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    if "table_name" in value:
        out["tableName"] = value["table_name"]
    if "type" in value:
        import aws_sdk_glue.types.table_optimizer_type

        out["type"] = aws_sdk_glue.types.table_optimizer_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetTableOptimizerEntry:
    out: BatchGetTableOptimizerEntry = {}  # type: ignore[typeddict-item]
    if "catalogId" in data:
        out["catalog_id"] = data["catalogId"]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    if "type" in data:
        import aws_sdk_glue.types.table_optimizer_type

        out["type"] = aws_sdk_glue.types.table_optimizer_type.deserialize_aws_json_1_1(
            data["type"]
        )
    return out
