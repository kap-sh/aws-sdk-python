"""Generated from Smithy shape ``com.amazonaws.lakeformation#DeleteDataCellsFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.name_string


class DeleteDataCellsFilterRequest(TypedDict, closed=True):
    table_catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The ID of the catalog to which the table belongs.</p>"""
    database_name: NotRequired["aws_sdk_lakeformation.types.name_string.NameString"]
    """<p>A database in the Glue Data Catalog.</p>"""
    table_name: NotRequired["aws_sdk_lakeformation.types.name_string.NameString"]
    """<p>A table in the database.</p>"""
    name: NotRequired["aws_sdk_lakeformation.types.name_string.NameString"]
    """<p>The name given by the user to the data filter cell.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataCellsFilterRequest) -> dict:
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


def deserialize_json(data: dict) -> DeleteDataCellsFilterRequest:
    out: DeleteDataCellsFilterRequest = {}  # type: ignore[typeddict-item]
    if "TableCatalogId" in data:
        out["table_catalog_id"] = data["TableCatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
