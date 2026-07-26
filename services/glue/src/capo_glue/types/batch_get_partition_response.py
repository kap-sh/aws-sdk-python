"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetPartitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.batch_get_partition_value_list
    import capo_glue.types.partition_list


class BatchGetPartitionResponse(TypedDict, closed=True):
    partitions: NotRequired["capo_glue.types.partition_list.PartitionList"]
    """<p>A list of the requested partitions.</p>"""
    unprocessed_keys: NotRequired[
        "capo_glue.types.batch_get_partition_value_list.BatchGetPartitionValueList"
    ]
    """<p>A list of the partition values in the request for which partitions were not returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetPartitionResponse) -> dict:
    out: dict = {}
    if "partitions" in value:
        import capo_glue.types.partition_list

        out["Partitions"] = capo_glue.types.partition_list.serialize_aws_json_1_1(
            value["partitions"]
        )
    if "unprocessed_keys" in value:
        import capo_glue.types.batch_get_partition_value_list

        out["UnprocessedKeys"] = (
            capo_glue.types.batch_get_partition_value_list.serialize_aws_json_1_1(
                value["unprocessed_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetPartitionResponse:
    out: BatchGetPartitionResponse = {}  # type: ignore[typeddict-item]
    if "Partitions" in data:
        import capo_glue.types.partition_list

        out["partitions"] = capo_glue.types.partition_list.deserialize_aws_json_1_1(
            data["Partitions"]
        )
    if "UnprocessedKeys" in data:
        import capo_glue.types.batch_get_partition_value_list

        out["unprocessed_keys"] = (
            capo_glue.types.batch_get_partition_value_list.deserialize_aws_json_1_1(
                data["UnprocessedKeys"]
            )
        )
    return out
