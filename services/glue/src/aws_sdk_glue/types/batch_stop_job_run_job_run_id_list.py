"""Generated from Smithy shape ``com.amazonaws.glue#BatchStopJobRunJobRunIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.id_string

BatchStopJobRunJobRunIdList: TypeAlias = list["aws_sdk_glue.types.id_string.IdString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchStopJobRunJobRunIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BatchStopJobRunJobRunIdList:
    return list(data)
