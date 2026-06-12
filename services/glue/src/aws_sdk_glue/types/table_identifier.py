"""Generated from Smithy shape ``com.amazonaws.glue#TableIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string


class TableIdentifier(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the table resides.</p>"""
    database_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the catalog database that contains the target table.</p>"""
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the target table.</p>"""
    region: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Region of the target table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableIdentifier) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TableIdentifier:
    out: TableIdentifier = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Region" in data:
        out["region"] = data["Region"]
    return out
