"""Generated from Smithy shape ``com.amazonaws.lakeformation#TableResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.name_string
    import aws_sdk_lakeformation.types.table_wildcard


class TableResource(TypedDict):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, it is the account ID of the caller.</p>"""
    database_name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal. </p>"""
    name: NotRequired["aws_sdk_lakeformation.types.name_string.NameString"]
    """<p>The name of the table.</p>"""
    table_wildcard: NotRequired[
        "aws_sdk_lakeformation.types.table_wildcard.TableWildcard"
    ]
    """<p>A wildcard object representing every table under a database.</p> <p>At least one of <code>TableResource$Name</code> or <code>TableResource$TableWildcard</code> is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableResource) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "table_wildcard" in value:
        import aws_sdk_lakeformation.types.table_wildcard

        out["TableWildcard"] = (
            aws_sdk_lakeformation.types.table_wildcard.serialize_json(
                value["table_wildcard"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableResource:
    out: TableResource = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("TableResource.database_name required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "TableWildcard" in data:
        import aws_sdk_lakeformation.types.table_wildcard

        out["table_wildcard"] = (
            aws_sdk_lakeformation.types.table_wildcard.deserialize_json(
                data["TableWildcard"]
            )
        )
    return out
