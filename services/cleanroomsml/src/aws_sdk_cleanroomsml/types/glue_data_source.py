"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GlueDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.account_id
    import aws_sdk_cleanroomsml.types.glue_database_name
    import aws_sdk_cleanroomsml.types.glue_table_name


class GlueDataSource(TypedDict, closed=True):
    table_name: "aws_sdk_cleanroomsml.types.glue_table_name.GlueTableName"
    """<p>The Glue table that contains the training data.</p>"""
    database_name: "aws_sdk_cleanroomsml.types.glue_database_name.GlueDatabaseName"
    """<p>The Glue database that contains the training data.</p>"""
    catalog_id: NotRequired["aws_sdk_cleanroomsml.types.account_id.AccountId"]
    """<p>The Glue catalog that contains the training data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueDataSource) -> dict:
    out: dict = {}
    out["tableName"] = value["table_name"]
    out["databaseName"] = value["database_name"]
    if "catalog_id" in value:
        out["catalogId"] = value["catalog_id"]
    return out


def deserialize_json(data: dict) -> GlueDataSource:
    out: GlueDataSource = {}  # type: ignore[typeddict-item]
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("GlueDataSource.table_name required")
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    else:
        raise DeserializationError("GlueDataSource.database_name required")
    if "catalogId" in data:
        out["catalog_id"] = data["catalogId"]
    return out
