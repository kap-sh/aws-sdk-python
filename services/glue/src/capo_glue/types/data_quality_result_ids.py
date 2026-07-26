"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.hash_string

DataQualityResultIds: TypeAlias = list["capo_glue.types.hash_string.HashString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DataQualityResultIds:
    return list(data)
