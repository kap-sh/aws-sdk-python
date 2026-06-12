"""Generated from Smithy shape ``com.amazonaws.glue#BatchTableOptimizers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.batch_table_optimizer

BatchTableOptimizers: TypeAlias = list[
    "aws_sdk_glue.types.batch_table_optimizer.BatchTableOptimizer"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchTableOptimizers) -> list:
    import aws_sdk_glue.types.batch_table_optimizer

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.batch_table_optimizer.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchTableOptimizers:
    import aws_sdk_glue.types.batch_table_optimizer

    out: BatchTableOptimizers = []
    for item in data:
        out.append(
            aws_sdk_glue.types.batch_table_optimizer.deserialize_aws_json_1_1(item)
        )
    return out
