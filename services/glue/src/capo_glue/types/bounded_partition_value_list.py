"""Generated from Smithy shape ``com.amazonaws.glue#BoundedPartitionValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.value_string

BoundedPartitionValueList: TypeAlias = list["capo_glue.types.value_string.ValueString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BoundedPartitionValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BoundedPartitionValueList:
    return list(data)
