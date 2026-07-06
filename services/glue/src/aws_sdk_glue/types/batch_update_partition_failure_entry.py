"""Generated from Smithy shape ``com.amazonaws.glue#BatchUpdatePartitionFailureEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.bounded_partition_value_list
    import aws_sdk_glue.types.error_detail


class BatchUpdatePartitionFailureEntry(TypedDict, closed=True):
    partition_value_list: NotRequired[
        "aws_sdk_glue.types.bounded_partition_value_list.BoundedPartitionValueList"
    ]
    """<p>A list of values defining the partitions.</p>"""
    error_detail: NotRequired["aws_sdk_glue.types.error_detail.ErrorDetail"]
    """<p>The details about the batch update partition error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdatePartitionFailureEntry) -> dict:
    out: dict = {}
    if "partition_value_list" in value:
        import aws_sdk_glue.types.bounded_partition_value_list

        out["PartitionValueList"] = (
            aws_sdk_glue.types.bounded_partition_value_list.serialize_aws_json_1_1(
                value["partition_value_list"]
            )
        )
    if "error_detail" in value:
        import aws_sdk_glue.types.error_detail

        out["ErrorDetail"] = aws_sdk_glue.types.error_detail.serialize_aws_json_1_1(
            value["error_detail"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchUpdatePartitionFailureEntry:
    out: BatchUpdatePartitionFailureEntry = {}  # type: ignore[typeddict-item]
    if "PartitionValueList" in data:
        import aws_sdk_glue.types.bounded_partition_value_list

        out["partition_value_list"] = (
            aws_sdk_glue.types.bounded_partition_value_list.deserialize_aws_json_1_1(
                data["PartitionValueList"]
            )
        )
    if "ErrorDetail" in data:
        import aws_sdk_glue.types.error_detail

        out["error_detail"] = aws_sdk_glue.types.error_detail.deserialize_aws_json_1_1(
            data["ErrorDetail"]
        )
    return out
