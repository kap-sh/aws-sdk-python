"""Generated from Smithy shape ``com.amazonaws.datapipeline#stringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_data_pipeline.types.string

stringList: TypeAlias = list["capo_data_pipeline.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: stringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> stringList:
    return list(data)
