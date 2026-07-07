"""Generated from Smithy shape ``com.amazonaws.glue#DatabaseIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string


class DatabaseIdentifier(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the database resides.</p>"""
    database_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the catalog database.</p>"""
    region: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>Region of the target database.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseIdentifier) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseIdentifier:
    out: DatabaseIdentifier = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "Region" in data:
        out["region"] = data["Region"]
    return out
