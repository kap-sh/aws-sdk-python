"""Generated from Smithy shape ``com.amazonaws.glue#BatchUpdatePartitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_update_partition_request_entry_list
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string


class BatchUpdatePartitionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the catalog in which the partition is to be updated. Currently, this should be the Amazon Web Services account ID.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the metadata database in which the partition is to be updated.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the metadata table in which the partition is to be updated.</p>"""
    entries: "aws_sdk_glue.types.batch_update_partition_request_entry_list.BatchUpdatePartitionRequestEntryList"
    """<p>A list of up to 100 <code>BatchUpdatePartitionRequestEntry</code> objects to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdatePartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import aws_sdk_glue.types.batch_update_partition_request_entry_list

    out["Entries"] = (
        aws_sdk_glue.types.batch_update_partition_request_entry_list.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchUpdatePartitionRequest:
    out: BatchUpdatePartitionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("BatchUpdatePartitionRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("BatchUpdatePartitionRequest.table_name required")
    if "Entries" in data:
        import aws_sdk_glue.types.batch_update_partition_request_entry_list

        out["entries"] = (
            aws_sdk_glue.types.batch_update_partition_request_entry_list.deserialize_aws_json_1_1(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError("BatchUpdatePartitionRequest.entries required")
    return out
