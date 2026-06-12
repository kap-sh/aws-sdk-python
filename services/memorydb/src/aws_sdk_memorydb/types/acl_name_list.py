"""Generated from Smithy shape ``com.amazonaws.memorydb#ACLNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.acl_name

ACLNameList: TypeAlias = list["aws_sdk_memorydb.types.acl_name.ACLName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ACLNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ACLNameList:
    return list(data)
