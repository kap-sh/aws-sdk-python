"""Generated from Smithy shape ``com.amazonaws.glue#BatchTableOptimizer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.database_name_string
    import capo_glue.types.table_name_string
    import capo_glue.types.table_optimizer


class BatchTableOptimizer(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The Catalog ID of the table.</p>"""
    database_name: NotRequired[
        "capo_glue.types.database_name_string.databaseNameString"
    ]
    """<p>The name of the database in the catalog in which the table resides.</p>"""
    table_name: NotRequired["capo_glue.types.table_name_string.tableNameString"]
    """<p>The name of the table.</p>"""
    table_optimizer: NotRequired["capo_glue.types.table_optimizer.TableOptimizer"]
    """<p>A <code>TableOptimizer</code> object that contains details on the configuration and last run of a table optimizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchTableOptimizer) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["catalogId"] = value["catalog_id"]
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    if "table_name" in value:
        out["tableName"] = value["table_name"]
    if "table_optimizer" in value:
        import capo_glue.types.table_optimizer

        out["tableOptimizer"] = capo_glue.types.table_optimizer.serialize_aws_json_1_1(
            value["table_optimizer"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchTableOptimizer:
    out: BatchTableOptimizer = {}  # type: ignore[typeddict-item]
    if "catalogId" in data:
        out["catalog_id"] = data["catalogId"]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    if "tableOptimizer" in data:
        import capo_glue.types.table_optimizer

        out["table_optimizer"] = (
            capo_glue.types.table_optimizer.deserialize_aws_json_1_1(
                data["tableOptimizer"]
            )
        )
    return out
