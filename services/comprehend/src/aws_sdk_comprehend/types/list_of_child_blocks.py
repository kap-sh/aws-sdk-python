"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfChildBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.child_block

ListOfChildBlocks: TypeAlias = list["aws_sdk_comprehend.types.child_block.ChildBlock"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfChildBlocks) -> list:
    import aws_sdk_comprehend.types.child_block

    out: list = []
    for item in value:
        out.append(aws_sdk_comprehend.types.child_block.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfChildBlocks:
    import aws_sdk_comprehend.types.child_block

    out: ListOfChildBlocks = []
    for item in data:
        out.append(aws_sdk_comprehend.types.child_block.deserialize_aws_json_1_1(item))
    return out
