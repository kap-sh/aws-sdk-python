"""Generated from Smithy shape ``com.amazonaws.comprehend#ChildBlock``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.string


class ChildBlock(TypedDict):
    child_block_id: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Unique identifier for the child block.</p>"""
    begin_offset: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>Offset of the start of the child block within its parent block.</p>"""
    end_offset: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>Offset of the end of the child block within its parent block.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChildBlock) -> dict:
    out: dict = {}
    if "child_block_id" in value:
        out["ChildBlockId"] = value["child_block_id"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ChildBlock:
    out: ChildBlock = {}  # type: ignore[typeddict-item]
    if "ChildBlockId" in data:
        out["child_block_id"] = data["ChildBlockId"]
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    return out
