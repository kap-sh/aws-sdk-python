"""Generated from Smithy shape ``com.amazonaws.glue#IcebergPartitionField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_name_string
    import aws_sdk_glue.types.iceberg_transform_string
    import aws_sdk_glue.types.integer


class IcebergPartitionField(TypedDict):
    source_id: "aws_sdk_glue.types.integer.Integer"
    """<p>The identifier of the source field from the table schema that this partition field is based on.</p>"""
    transform: "aws_sdk_glue.types.iceberg_transform_string.IcebergTransformString"
    """<p>The transformation function applied to the source field to create the partition, such as identity, bucket, truncate, year, month, day, or hour.</p>"""
    name: "aws_sdk_glue.types.column_name_string.ColumnNameString"
    """<p>The name of the partition field as it will appear in the partitioned table structure.</p>"""
    field_id: "aws_sdk_glue.types.integer.Integer"
    """<p>The unique identifier assigned to this partition field within the Iceberg table's partition specification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergPartitionField) -> dict:
    out: dict = {}
    out["SourceId"] = value.get("source_id", 0)
    out["Transform"] = value["transform"]
    out["Name"] = value["name"]
    out["FieldId"] = value.get("field_id", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergPartitionField:
    out: IcebergPartitionField = {}  # type: ignore[typeddict-item]
    if "SourceId" in data:
        out["source_id"] = data["SourceId"]
    else:
        out["source_id"] = 0
    if "Transform" in data:
        out["transform"] = data["Transform"]
    else:
        raise DeserializationError("IcebergPartitionField.transform required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("IcebergPartitionField.name required")
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = 0
    return out
