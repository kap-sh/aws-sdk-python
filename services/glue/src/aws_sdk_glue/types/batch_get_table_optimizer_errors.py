"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetTableOptimizerErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_get_table_optimizer_error

BatchGetTableOptimizerErrors: TypeAlias = list[
    "aws_sdk_glue.types.batch_get_table_optimizer_error.BatchGetTableOptimizerError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetTableOptimizerErrors) -> list:
    import aws_sdk_glue.types.batch_get_table_optimizer_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.batch_get_table_optimizer_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchGetTableOptimizerErrors:
    import aws_sdk_glue.types.batch_get_table_optimizer_error

    out: BatchGetTableOptimizerErrors = []
    for item in data:
        out.append(
            aws_sdk_glue.types.batch_get_table_optimizer_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
