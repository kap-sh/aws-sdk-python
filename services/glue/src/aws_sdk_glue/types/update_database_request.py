"""Generated from Smithy shape ``com.amazonaws.glue#UpdateDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.database_input
    import aws_sdk_glue.types.name_string


class UpdateDatabaseRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the metadata database resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the database to update in the catalog. For Hive compatibility, this is folded to lowercase.</p>"""
    database_input: "aws_sdk_glue.types.database_input.DatabaseInput"
    """<p>A <code>DatabaseInput</code> object specifying the new definition of the metadata database in the catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDatabaseRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["Name"] = value["name"]
    import aws_sdk_glue.types.database_input

    out["DatabaseInput"] = aws_sdk_glue.types.database_input.serialize_aws_json_1_1(
        value["database_input"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDatabaseRequest:
    out: UpdateDatabaseRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDatabaseRequest.name required")
    if "DatabaseInput" in data:
        import aws_sdk_glue.types.database_input

        out["database_input"] = (
            aws_sdk_glue.types.database_input.deserialize_aws_json_1_1(
                data["DatabaseInput"]
            )
        )
    else:
        raise DeserializationError("UpdateDatabaseRequest.database_input required")
    return out
