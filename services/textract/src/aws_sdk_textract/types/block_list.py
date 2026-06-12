"""Generated from Smithy shape ``com.amazonaws.textract#BlockList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.block

BlockList: TypeAlias = list["aws_sdk_textract.types.block.Block"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockList) -> list:
    import aws_sdk_textract.types.block

    out: list = []
    for item in value:
        out.append(aws_sdk_textract.types.block.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BlockList:
    import aws_sdk_textract.types.block

    out: BlockList = []
    for item in data:
        out.append(aws_sdk_textract.types.block.deserialize_aws_json_1_1(item))
    return out
