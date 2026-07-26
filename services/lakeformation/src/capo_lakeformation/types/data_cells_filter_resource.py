"""Generated from Smithy shape ``com.amazonaws.lakeformation#DataCellsFilterResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.name_string


class DataCellsFilterResource(TypedDict, closed=True):
    table_catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The ID of the catalog to which the table belongs.</p>"""
    database_name: NotRequired["capo_lakeformation.types.name_string.NameString"]
    """<p>A database in the Glue Data Catalog.</p>"""
    table_name: NotRequired["capo_lakeformation.types.name_string.NameString"]
    """<p>The name of the table.</p>"""
    name: NotRequired["capo_lakeformation.types.name_string.NameString"]
    """<p>The name of the data cells filter. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataCellsFilterResource) -> dict:
    out: dict = {}
    if "table_catalog_id" in value:
        out["TableCatalogId"] = value["table_catalog_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DataCellsFilterResource:
    out: DataCellsFilterResource = {}  # type: ignore[typeddict-item]
    if "TableCatalogId" in data:
        out["table_catalog_id"] = data["TableCatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
