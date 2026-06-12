"""Generated from Smithy shape ``com.amazonaws.memorydb#ACLList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.acl

ACLList: TypeAlias = list["aws_sdk_memorydb.types.acl.ACL"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ACLList) -> list:
    import aws_sdk_memorydb.types.acl

    out: list = []
    for item in value:
        out.append(aws_sdk_memorydb.types.acl.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ACLList:
    import aws_sdk_memorydb.types.acl

    out: ACLList = []
    for item in data:
        out.append(aws_sdk_memorydb.types.acl.deserialize_aws_json_1_1(item))
    return out
