"""Generated from Smithy shape ``com.amazonaws.glue#IcebergPartitionSpec``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.iceberg_partition_spec_field_list
    import aws_sdk_glue.types.integer


class IcebergPartitionSpec(TypedDict):
    fields: "aws_sdk_glue.types.iceberg_partition_spec_field_list.IcebergPartitionSpecFieldList"
    """<p>The list of partition fields that define how the table data should be partitioned, including source fields and their transformations.</p>"""
    spec_id: "aws_sdk_glue.types.integer.Integer"
    """<p>The unique identifier for this partition specification within the Iceberg table's metadata history.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergPartitionSpec) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.iceberg_partition_spec_field_list

    out["Fields"] = (
        aws_sdk_glue.types.iceberg_partition_spec_field_list.serialize_aws_json_1_1(
            value["fields"]
        )
    )
    out["SpecId"] = value.get("spec_id", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergPartitionSpec:
    out: IcebergPartitionSpec = {}  # type: ignore[typeddict-item]
    if "Fields" in data:
        import aws_sdk_glue.types.iceberg_partition_spec_field_list

        out["fields"] = (
            aws_sdk_glue.types.iceberg_partition_spec_field_list.deserialize_aws_json_1_1(
                data["Fields"]
            )
        )
    else:
        raise DeserializationError("IcebergPartitionSpec.fields required")
    if "SpecId" in data:
        out["spec_id"] = data["SpecId"]
    else:
        out["spec_id"] = 0
    return out
