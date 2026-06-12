"""Generated from Smithy shape ``com.amazonaws.datapipeline#idList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.id

idList: TypeAlias = list["aws_sdk_data_pipeline.types.id.id"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: idList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> idList:
    return list(data)
