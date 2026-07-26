"""Generated from Smithy shape ``com.amazonaws.memorydb#NodeTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.string

NodeTypeList: TypeAlias = list["capo_memorydb.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeTypeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> NodeTypeList:
    return list(data)
