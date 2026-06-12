"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetTableOptimizerEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_get_table_optimizer_entry

BatchGetTableOptimizerEntries: TypeAlias = list[
    "aws_sdk_glue.types.batch_get_table_optimizer_entry.BatchGetTableOptimizerEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetTableOptimizerEntries) -> list:
    import aws_sdk_glue.types.batch_get_table_optimizer_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.batch_get_table_optimizer_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchGetTableOptimizerEntries:
    import aws_sdk_glue.types.batch_get_table_optimizer_entry

    out: BatchGetTableOptimizerEntries = []
    for item in data:
        out.append(
            aws_sdk_glue.types.batch_get_table_optimizer_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
