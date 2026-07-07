"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergPartitionSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.iceberg_partition_field_list


class IcebergPartitionSpec(TypedDict, closed=True):
    fields: (
        "aws_sdk_s3tables.types.iceberg_partition_field_list.IcebergPartitionFieldList"
    )
    """<p>The list of partition fields that define how the table data is partitioned. Each field specifies a source field and a transform to apply. This field is required if <code>partitionSpec</code> is provided.</p>"""
    spec_id: NotRequired["int"]
    """<p>The unique identifier for this partition specification. If not specified, defaults to <code>0</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcebergPartitionSpec) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.iceberg_partition_field_list

    out["fields"] = aws_sdk_s3tables.types.iceberg_partition_field_list.serialize_json(
        value["fields"]
    )
    if "spec_id" in value:
        out["spec-id"] = value["spec_id"]
    return out


def deserialize_json(data: dict) -> IcebergPartitionSpec:
    out: IcebergPartitionSpec = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import aws_sdk_s3tables.types.iceberg_partition_field_list

        out["fields"] = (
            aws_sdk_s3tables.types.iceberg_partition_field_list.deserialize_json(
                data["fields"]
            )
        )
    else:
        raise DeserializationError("IcebergPartitionSpec.fields required")
    if "spec-id" in data:
        out["spec_id"] = data["spec-id"]
    return out
