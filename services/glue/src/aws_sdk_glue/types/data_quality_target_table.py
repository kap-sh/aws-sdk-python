"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityTargetTable``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string


class DataQualityTargetTable(TypedDict):
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the Glue table.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the database where the Glue table exists.</p>"""
    catalog_id: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The catalog id where the Glue table exists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityTargetTable) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    out["DatabaseName"] = value["database_name"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityTargetTable:
    out: DataQualityTargetTable = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("DataQualityTargetTable.table_name required")
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("DataQualityTargetTable.database_name required")
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    return out
