"""Generated from Smithy shape ``com.amazonaws.glue#UpdatePartitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.bounded_partition_value_list
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.partition_input


class UpdatePartitionRequest(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the partition to be updated resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the catalog database in which the table in question resides.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the table in which the partition to be updated is located.</p>"""
    partition_value_list: (
        "aws_sdk_glue.types.bounded_partition_value_list.BoundedPartitionValueList"
    )
    """<p>List of partition key values that define the partition to update.</p>"""
    partition_input: "aws_sdk_glue.types.partition_input.PartitionInput"
    """<p>The new partition object to update the partition to.</p> <p>The <code>Values</code> property can't be changed. If you want to change the partition key values for a partition, delete and recreate the partition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import aws_sdk_glue.types.bounded_partition_value_list

    out["PartitionValueList"] = (
        aws_sdk_glue.types.bounded_partition_value_list.serialize_aws_json_1_1(
            value["partition_value_list"]
        )
    )
    import aws_sdk_glue.types.partition_input

    out["PartitionInput"] = aws_sdk_glue.types.partition_input.serialize_aws_json_1_1(
        value["partition_input"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePartitionRequest:
    out: UpdatePartitionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("UpdatePartitionRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("UpdatePartitionRequest.table_name required")
    if "PartitionValueList" in data:
        import aws_sdk_glue.types.bounded_partition_value_list

        out["partition_value_list"] = (
            aws_sdk_glue.types.bounded_partition_value_list.deserialize_aws_json_1_1(
                data["PartitionValueList"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePartitionRequest.partition_value_list required"
        )
    if "PartitionInput" in data:
        import aws_sdk_glue.types.partition_input

        out["partition_input"] = (
            aws_sdk_glue.types.partition_input.deserialize_aws_json_1_1(
                data["PartitionInput"]
            )
        )
    else:
        raise DeserializationError("UpdatePartitionRequest.partition_input required")
    return out
