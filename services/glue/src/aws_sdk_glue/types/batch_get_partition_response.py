"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetPartitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_get_partition_value_list
    import aws_sdk_glue.types.partition_list


class BatchGetPartitionResponse(TypedDict, closed=True):
    partitions: NotRequired["aws_sdk_glue.types.partition_list.PartitionList"]
    """<p>A list of the requested partitions.</p>"""
    unprocessed_keys: NotRequired[
        "aws_sdk_glue.types.batch_get_partition_value_list.BatchGetPartitionValueList"
    ]
    """<p>A list of the partition values in the request for which partitions were not returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetPartitionResponse) -> dict:
    out: dict = {}
    if "partitions" in value:
        import aws_sdk_glue.types.partition_list

        out["Partitions"] = aws_sdk_glue.types.partition_list.serialize_aws_json_1_1(
            value["partitions"]
        )
    if "unprocessed_keys" in value:
        import aws_sdk_glue.types.batch_get_partition_value_list

        out["UnprocessedKeys"] = (
            aws_sdk_glue.types.batch_get_partition_value_list.serialize_aws_json_1_1(
                value["unprocessed_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetPartitionResponse:
    out: BatchGetPartitionResponse = {}  # type: ignore[typeddict-item]
    if "Partitions" in data:
        import aws_sdk_glue.types.partition_list

        out["partitions"] = aws_sdk_glue.types.partition_list.deserialize_aws_json_1_1(
            data["Partitions"]
        )
    if "UnprocessedKeys" in data:
        import aws_sdk_glue.types.batch_get_partition_value_list

        out["unprocessed_keys"] = (
            aws_sdk_glue.types.batch_get_partition_value_list.deserialize_aws_json_1_1(
                data["UnprocessedKeys"]
            )
        )
    return out
