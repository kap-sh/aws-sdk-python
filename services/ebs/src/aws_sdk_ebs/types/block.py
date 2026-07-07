"""Generated from Smithy shape ``com.amazonaws.ebs#Block``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ebs.types.block_index
    import aws_sdk_ebs.types.block_token


class Block(TypedDict, closed=True):
    block_index: NotRequired["aws_sdk_ebs.types.block_index.BlockIndex"]
    """<p>The block index.</p>"""
    block_token: NotRequired["aws_sdk_ebs.types.block_token.BlockToken"]
    """<p>The block token for the block index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Block) -> dict:
    out: dict = {}
    if "block_index" in value:
        out["BlockIndex"] = value["block_index"]
    if "block_token" in value:
        out["BlockToken"] = value["block_token"]
    return out


def deserialize_json(data: dict) -> Block:
    out: Block = {}  # type: ignore[typeddict-item]
    if "BlockIndex" in data:
        out["block_index"] = data["BlockIndex"]
    if "BlockToken" in data:
        out["block_token"] = data["BlockToken"]
    return out
