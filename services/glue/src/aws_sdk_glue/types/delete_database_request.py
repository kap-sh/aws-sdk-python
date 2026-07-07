"""Generated from Smithy shape ``com.amazonaws.glue#DeleteDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string


class DeleteDatabaseRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the database resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the database to delete. For Hive compatibility, this must be all lowercase.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDatabaseRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDatabaseRequest:
    out: DeleteDatabaseRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteDatabaseRequest.name required")
    return out
