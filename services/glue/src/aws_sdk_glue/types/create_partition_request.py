"""Generated from Smithy shape ``com.amazonaws.glue#CreatePartitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.partition_input


class CreatePartitionRequest(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The Amazon Web Services account ID of the catalog in which the partition is to be created.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the metadata database in which the partition is to be created.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the metadata table in which the partition is to be created.</p>"""
    partition_input: "aws_sdk_glue.types.partition_input.PartitionInput"
    """<p>A <code>PartitionInput</code> structure defining the partition to be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import aws_sdk_glue.types.partition_input

    out["PartitionInput"] = aws_sdk_glue.types.partition_input.serialize_aws_json_1_1(
        value["partition_input"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePartitionRequest:
    out: CreatePartitionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("CreatePartitionRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("CreatePartitionRequest.table_name required")
    if "PartitionInput" in data:
        import aws_sdk_glue.types.partition_input

        out["partition_input"] = (
            aws_sdk_glue.types.partition_input.deserialize_aws_json_1_1(
                data["PartitionInput"]
            )
        )
    else:
        raise DeserializationError("CreatePartitionRequest.partition_input required")
    return out
