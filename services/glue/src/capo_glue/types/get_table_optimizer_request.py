"""Generated from Smithy shape ``com.amazonaws.glue#GetTableOptimizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.table_optimizer_type


class GetTableOptimizerRequest(TypedDict, closed=True):
    catalog_id: "capo_glue.types.catalog_id_string.CatalogIdString"
    """<p>The Catalog ID of the table.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the database in the catalog in which the table resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table.</p>"""
    type: "capo_glue.types.table_optimizer_type.TableOptimizerType"
    """<p>The type of table optimizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableOptimizerRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.table_optimizer_type

    out["Type"] = capo_glue.types.table_optimizer_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableOptimizerRequest:
    out: GetTableOptimizerRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError("GetTableOptimizerRequest.catalog_id required")
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("GetTableOptimizerRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("GetTableOptimizerRequest.table_name required")
    if "Type" in data:
        import capo_glue.types.table_optimizer_type

        out["type"] = capo_glue.types.table_optimizer_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("GetTableOptimizerRequest.type required")
    return out
