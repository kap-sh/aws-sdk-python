"""Generated from Smithy shape ``com.amazonaws.glue#BatchCreatePartitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.partition_input_list


class BatchCreatePartitionRequest(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the catalog in which the partition is to be created. Currently, this should be the Amazon Web Services account ID.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the metadata database in which the partition is to be created.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the metadata table in which the partition is to be created.</p>"""
    partition_input_list: "aws_sdk_glue.types.partition_input_list.PartitionInputList"
    """<p>A list of <code>PartitionInput</code> structures that define the partitions to be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchCreatePartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import aws_sdk_glue.types.partition_input_list

    out["PartitionInputList"] = (
        aws_sdk_glue.types.partition_input_list.serialize_aws_json_1_1(
            value["partition_input_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchCreatePartitionRequest:
    out: BatchCreatePartitionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("BatchCreatePartitionRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("BatchCreatePartitionRequest.table_name required")
    if "PartitionInputList" in data:
        import aws_sdk_glue.types.partition_input_list

        out["partition_input_list"] = (
            aws_sdk_glue.types.partition_input_list.deserialize_aws_json_1_1(
                data["PartitionInputList"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreatePartitionRequest.partition_input_list required"
        )
    return out
