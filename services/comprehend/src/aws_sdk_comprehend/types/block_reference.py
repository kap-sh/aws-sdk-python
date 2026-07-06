"""Generated from Smithy shape ``com.amazonaws.comprehend#BlockReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.list_of_child_blocks
    import aws_sdk_comprehend.types.string


class BlockReference(TypedDict, closed=True):
    block_id: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Unique identifier for the block.</p>"""
    begin_offset: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>Offset of the start of the block within its parent block.</p>"""
    end_offset: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>Offset of the end of the block within its parent block.</p>"""
    child_blocks: NotRequired[
        "aws_sdk_comprehend.types.list_of_child_blocks.ListOfChildBlocks"
    ]
    """<p>List of child blocks within this block.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockReference) -> dict:
    out: dict = {}
    if "block_id" in value:
        out["BlockId"] = value["block_id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "child_blocks" in value:
        import aws_sdk_comprehend.types.list_of_child_blocks

        out["ChildBlocks"] = (
            aws_sdk_comprehend.types.list_of_child_blocks.serialize_aws_json_1_1(
                value["child_blocks"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BlockReference:
    out: BlockReference = {}  # type: ignore[typeddict-item]
    if "BlockId" in data:
        out["block_id"] = data["BlockId"]
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    if "ChildBlocks" in data:
        import aws_sdk_comprehend.types.list_of_child_blocks

        out["child_blocks"] = (
            aws_sdk_comprehend.types.list_of_child_blocks.deserialize_aws_json_1_1(
                data["ChildBlocks"]
            )
        )
    return out
