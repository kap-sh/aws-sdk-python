"""Generated from Smithy shape ``com.amazonaws.memorydb#ReservedNodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.reserved_node

ReservedNodeList: TypeAlias = list["capo_memorydb.types.reserved_node.ReservedNode"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservedNodeList) -> list:
    import capo_memorydb.types.reserved_node

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.reserved_node.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ReservedNodeList:
    import capo_memorydb.types.reserved_node

    out: ReservedNodeList = []
    for item in data:
        out.append(capo_memorydb.types.reserved_node.deserialize_aws_json_1_1(item))
    return out
