"""Generated from Smithy shape ``com.amazonaws.glue#GetTableOptimizerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.table_optimizer


class GetTableOptimizerResponse(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The Catalog ID of the table.</p>"""
    database_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the database in the catalog in which the table resides.</p>"""
    table_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the table.</p>"""
    table_optimizer: NotRequired["capo_glue.types.table_optimizer.TableOptimizer"]
    """<p>The optimizer associated with the specified table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableOptimizerResponse) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "table_optimizer" in value:
        import capo_glue.types.table_optimizer

        out["TableOptimizer"] = capo_glue.types.table_optimizer.serialize_aws_json_1_1(
            value["table_optimizer"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableOptimizerResponse:
    out: GetTableOptimizerResponse = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "TableOptimizer" in data:
        import capo_glue.types.table_optimizer

        out["table_optimizer"] = (
            capo_glue.types.table_optimizer.deserialize_aws_json_1_1(
                data["TableOptimizer"]
            )
        )
    return out
