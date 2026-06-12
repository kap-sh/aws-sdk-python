"""Generated from Smithy shape ``com.amazonaws.glue#BatchUpdatePartitionRequestEntry``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.bounded_partition_value_list
    import aws_sdk_glue.types.partition_input


class BatchUpdatePartitionRequestEntry(TypedDict):
    partition_value_list: (
        "aws_sdk_glue.types.bounded_partition_value_list.BoundedPartitionValueList"
    )
    """<p>A list of values defining the partitions.</p>"""
    partition_input: "aws_sdk_glue.types.partition_input.PartitionInput"
    """<p>The structure used to update a partition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdatePartitionRequestEntry) -> dict:
    out: dict = {}
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


def deserialize_aws_json_1_1(data: dict) -> BatchUpdatePartitionRequestEntry:
    out: BatchUpdatePartitionRequestEntry = {}  # type: ignore[typeddict-item]
    if "PartitionValueList" in data:
        import aws_sdk_glue.types.bounded_partition_value_list

        out["partition_value_list"] = (
            aws_sdk_glue.types.bounded_partition_value_list.deserialize_aws_json_1_1(
                data["PartitionValueList"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdatePartitionRequestEntry.partition_value_list required"
        )
    if "PartitionInput" in data:
        import aws_sdk_glue.types.partition_input

        out["partition_input"] = (
            aws_sdk_glue.types.partition_input.deserialize_aws_json_1_1(
                data["PartitionInput"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdatePartitionRequestEntry.partition_input required"
        )
    return out
