"""Generated from Smithy shape ``com.amazonaws.glue#CreatePartitionIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.partition_index


class CreatePartitionIndexRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The catalog ID where the table resides.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Specifies the name of a database in which you want to create a partition index.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>Specifies the name of a table in which you want to create a partition index.</p>"""
    partition_index: "aws_sdk_glue.types.partition_index.PartitionIndex"
    """<p>Specifies a <code>PartitionIndex</code> structure to create a partition index in an existing table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePartitionIndexRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import aws_sdk_glue.types.partition_index

    out["PartitionIndex"] = aws_sdk_glue.types.partition_index.serialize_aws_json_1_1(
        value["partition_index"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePartitionIndexRequest:
    out: CreatePartitionIndexRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("CreatePartitionIndexRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("CreatePartitionIndexRequest.table_name required")
    if "PartitionIndex" in data:
        import aws_sdk_glue.types.partition_index

        out["partition_index"] = (
            aws_sdk_glue.types.partition_index.deserialize_aws_json_1_1(
                data["PartitionIndex"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePartitionIndexRequest.partition_index required"
        )
    return out
