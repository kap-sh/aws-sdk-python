"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetDataCellsFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.name_string


class GetDataCellsFilterRequest(TypedDict, closed=True):
    table_catalog_id: "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    """<p>The ID of the catalog to which the table belongs.</p>"""
    database_name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>A database in the Glue Data Catalog.</p>"""
    table_name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>A table in the database.</p>"""
    name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>The name given by the user to the data filter cell.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataCellsFilterRequest) -> dict:
    out: dict = {}
    out["TableCatalogId"] = value["table_catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> GetDataCellsFilterRequest:
    out: GetDataCellsFilterRequest = {}  # type: ignore[typeddict-item]
    if "TableCatalogId" in data:
        out["table_catalog_id"] = data["TableCatalogId"]
    else:
        raise DeserializationError(
            "GetDataCellsFilterRequest.table_catalog_id required"
        )
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("GetDataCellsFilterRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("GetDataCellsFilterRequest.table_name required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetDataCellsFilterRequest.name required")
    return out
