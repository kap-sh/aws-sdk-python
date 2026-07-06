"""Generated from Smithy shape ``com.amazonaws.glue#DeleteColumnStatisticsForTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string


class DeleteColumnStatisticsForTableRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the catalog database where the partitions reside.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the partitions' table.</p>"""
    column_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteColumnStatisticsForTableRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    out["ColumnName"] = value["column_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteColumnStatisticsForTableRequest:
    out: DeleteColumnStatisticsForTableRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "DeleteColumnStatisticsForTableRequest.database_name required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "DeleteColumnStatisticsForTableRequest.table_name required"
        )
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    else:
        raise DeserializationError(
            "DeleteColumnStatisticsForTableRequest.column_name required"
        )
    return out
