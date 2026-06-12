"""Generated from Smithy shape ``com.amazonaws.lakeformation#DatabaseResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.name_string


class DatabaseResource(TypedDict):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, it is the account ID of the caller.</p>"""
    name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>The name of the database resource. Unique to the Data Catalog.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseResource) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DatabaseResource:
    out: DatabaseResource = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DatabaseResource.name required")
    return out
