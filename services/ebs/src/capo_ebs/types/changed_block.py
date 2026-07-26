"""Generated from Smithy shape ``com.amazonaws.ebs#ChangedBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ebs.types.block_index
    import capo_ebs.types.block_token


class ChangedBlock(TypedDict, closed=True):
    block_index: NotRequired["capo_ebs.types.block_index.BlockIndex"]
    """<p>The block index.</p>"""
    first_block_token: NotRequired["capo_ebs.types.block_token.BlockToken"]
    """<p>The block token for the block index of the <code>FirstSnapshotId</code> specified in the <code>ListChangedBlocks</code> operation. This value is absent if the first snapshot does not have the changed block that is on the second snapshot.</p>"""
    second_block_token: NotRequired["capo_ebs.types.block_token.BlockToken"]
    """<p>The block token for the block index of the <code>SecondSnapshotId</code> specified in the <code>ListChangedBlocks</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangedBlock) -> dict:
    out: dict = {}
    if "block_index" in value:
        out["BlockIndex"] = value["block_index"]
    if "first_block_token" in value:
        out["FirstBlockToken"] = value["first_block_token"]
    if "second_block_token" in value:
        out["SecondBlockToken"] = value["second_block_token"]
    return out


def deserialize_json(data: dict) -> ChangedBlock:
    out: ChangedBlock = {}  # type: ignore[typeddict-item]
    if "BlockIndex" in data:
        out["block_index"] = data["BlockIndex"]
    if "FirstBlockToken" in data:
        out["first_block_token"] = data["FirstBlockToken"]
    if "SecondBlockToken" in data:
        out["second_block_token"] = data["SecondBlockToken"]
    return out
