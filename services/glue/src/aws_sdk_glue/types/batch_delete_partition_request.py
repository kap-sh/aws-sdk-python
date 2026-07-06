"""Generated from Smithy shape ``com.amazonaws.glue#BatchDeletePartitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_delete_partition_value_list
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string


class BatchDeletePartitionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the partition to be deleted resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the catalog database in which the table in question resides.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the table that contains the partitions to be deleted.</p>"""
    partitions_to_delete: "aws_sdk_glue.types.batch_delete_partition_value_list.BatchDeletePartitionValueList"
    """<p>A list of <code>PartitionInput</code> structures that define the partitions to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeletePartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import aws_sdk_glue.types.batch_delete_partition_value_list

    out["PartitionsToDelete"] = (
        aws_sdk_glue.types.batch_delete_partition_value_list.serialize_aws_json_1_1(
            value["partitions_to_delete"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeletePartitionRequest:
    out: BatchDeletePartitionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("BatchDeletePartitionRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("BatchDeletePartitionRequest.table_name required")
    if "PartitionsToDelete" in data:
        import aws_sdk_glue.types.batch_delete_partition_value_list

        out["partitions_to_delete"] = (
            aws_sdk_glue.types.batch_delete_partition_value_list.deserialize_aws_json_1_1(
                data["PartitionsToDelete"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeletePartitionRequest.partitions_to_delete required"
        )
    return out
