"""Generated from Smithy shape ``com.amazonaws.glue#PartitionErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.partition_error

PartitionErrors: TypeAlias = list["capo_glue.types.partition_error.PartitionError"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionErrors) -> list:
    import capo_glue.types.partition_error

    out: list = []
    for item in value:
        out.append(capo_glue.types.partition_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PartitionErrors:
    import capo_glue.types.partition_error

    out: PartitionErrors = []
    for item in data:
        out.append(capo_glue.types.partition_error.deserialize_aws_json_1_1(item))
    return out
