"""Generated from Smithy shape ``com.amazonaws.glue#TransformIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.hash_string

TransformIdList: TypeAlias = list["capo_glue.types.hash_string.HashString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TransformIdList:
    return list(data)
