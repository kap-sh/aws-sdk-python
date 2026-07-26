"""Generated from Smithy shape ``com.amazonaws.glue#DeleteTableVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.version_string


class DeleteTableVersionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table. For Hive compatibility, this name is entirely lowercase.</p>"""
    version_id: "capo_glue.types.version_string.VersionString"
    """<p>The ID of the table version to be deleted. A <code>VersionID</code> is a string representation of an integer. Each version is incremented by 1.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTableVersionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    out["VersionId"] = value["version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTableVersionRequest:
    out: DeleteTableVersionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("DeleteTableVersionRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("DeleteTableVersionRequest.table_name required")
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    else:
        raise DeserializationError("DeleteTableVersionRequest.version_id required")
    return out
