"""Generated from Smithy shape ``com.amazonaws.memorydb#ParameterNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string

ParameterNameList: TypeAlias = list["aws_sdk_memorydb.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ParameterNameList:
    return list(data)
