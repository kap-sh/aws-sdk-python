"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetTableOptimizerError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.database_name_string
    import capo_glue.types.error_detail
    import capo_glue.types.table_name_string
    import capo_glue.types.table_optimizer_type


class BatchGetTableOptimizerError(TypedDict, closed=True):
    error: NotRequired["capo_glue.types.error_detail.ErrorDetail"]
    """<p>An <code>ErrorDetail</code> object containing code and message details about the error.</p>"""
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The Catalog ID of the table.</p>"""
    database_name: NotRequired[
        "capo_glue.types.database_name_string.databaseNameString"
    ]
    """<p>The name of the database in the catalog in which the table resides.</p>"""
    table_name: NotRequired["capo_glue.types.table_name_string.tableNameString"]
    """<p>The name of the table.</p>"""
    type: NotRequired["capo_glue.types.table_optimizer_type.TableOptimizerType"]
    """<p>The type of table optimizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetTableOptimizerError) -> dict:
    out: dict = {}
    if "error" in value:
        import capo_glue.types.error_detail

        out["error"] = capo_glue.types.error_detail.serialize_aws_json_1_1(
            value["error"]
        )
    if "catalog_id" in value:
        out["catalogId"] = value["catalog_id"]
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    if "table_name" in value:
        out["tableName"] = value["table_name"]
    if "type" in value:
        import capo_glue.types.table_optimizer_type

        out["type"] = capo_glue.types.table_optimizer_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetTableOptimizerError:
    out: BatchGetTableOptimizerError = {}  # type: ignore[typeddict-item]
    if "error" in data:
        import capo_glue.types.error_detail

        out["error"] = capo_glue.types.error_detail.deserialize_aws_json_1_1(
            data["error"]
        )
    if "catalogId" in data:
        out["catalog_id"] = data["catalogId"]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    if "type" in data:
        import capo_glue.types.table_optimizer_type

        out["type"] = capo_glue.types.table_optimizer_type.deserialize_aws_json_1_1(
            data["type"]
        )
    return out
