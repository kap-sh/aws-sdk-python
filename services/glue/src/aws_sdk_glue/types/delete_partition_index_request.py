"""Generated from Smithy shape ``com.amazonaws.glue#DeletePartitionIndexRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string


class DeletePartitionIndexRequest(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The catalog ID where the table resides.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Specifies the name of a database from which you want to delete a partition index.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Specifies the name of a table from which you want to delete a partition index.</p>"""
    index_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the partition index to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePartitionIndexRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    out["IndexName"] = value["index_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePartitionIndexRequest:
    out: DeletePartitionIndexRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("DeletePartitionIndexRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("DeletePartitionIndexRequest.table_name required")
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError("DeletePartitionIndexRequest.index_name required")
    return out
