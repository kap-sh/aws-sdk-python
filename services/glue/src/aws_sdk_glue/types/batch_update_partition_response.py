"""Generated from Smithy shape ``com.amazonaws.glue#BatchUpdatePartitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_update_partition_failure_list


class BatchUpdatePartitionResponse(TypedDict):
    errors: NotRequired[
        "aws_sdk_glue.types.batch_update_partition_failure_list.BatchUpdatePartitionFailureList"
    ]
    """<p>The errors encountered when trying to update the requested partitions. A list of <code>BatchUpdatePartitionFailureEntry</code> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdatePartitionResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_glue.types.batch_update_partition_failure_list

        out["Errors"] = (
            aws_sdk_glue.types.batch_update_partition_failure_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchUpdatePartitionResponse:
    out: BatchUpdatePartitionResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_glue.types.batch_update_partition_failure_list

        out["errors"] = (
            aws_sdk_glue.types.batch_update_partition_failure_list.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    return out
