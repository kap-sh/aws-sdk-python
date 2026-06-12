"""Generated from Smithy shape ``com.amazonaws.memorydb#ACLClusterNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string

ACLClusterNameList: TypeAlias = list["aws_sdk_memorydb.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ACLClusterNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ACLClusterNameList:
    return list(data)
