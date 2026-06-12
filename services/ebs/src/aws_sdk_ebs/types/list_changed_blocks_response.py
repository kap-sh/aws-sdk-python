"""Generated from Smithy shape ``com.amazonaws.ebs#ListChangedBlocksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ebs.types.block_size
    import aws_sdk_ebs.types.changed_blocks
    import aws_sdk_ebs.types.page_token
    import aws_sdk_ebs.types.time_stamp
    import aws_sdk_ebs.types.volume_size


class ListChangedBlocksResponse(TypedDict):
    changed_blocks: NotRequired["aws_sdk_ebs.types.changed_blocks.ChangedBlocks"]
    """<p>An array of objects containing information about the changed blocks.</p>"""
    expiry_time: NotRequired["aws_sdk_ebs.types.time_stamp.TimeStamp"]
    """<p>The time when the <code>BlockToken</code> expires.</p>"""
    volume_size: NotRequired["aws_sdk_ebs.types.volume_size.VolumeSize"]
    """<p>The size of the volume in GB.</p>"""
    block_size: NotRequired["aws_sdk_ebs.types.block_size.BlockSize"]
    """<p>The size of the blocks in the snapshot, in bytes.</p>"""
    next_token: NotRequired["aws_sdk_ebs.types.page_token.PageToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChangedBlocksResponse) -> dict:
    out: dict = {}
    if "changed_blocks" in value:
        import aws_sdk_ebs.types.changed_blocks

        out["ChangedBlocks"] = aws_sdk_ebs.types.changed_blocks.serialize_json(
            value["changed_blocks"]
        )
    if "expiry_time" in value:
        import aws_sdk_ebs.types.time_stamp

        out["ExpiryTime"] = aws_sdk_ebs.types.time_stamp.serialize_json(
            value["expiry_time"]
        )
    if "volume_size" in value:
        out["VolumeSize"] = value["volume_size"]
    if "block_size" in value:
        out["BlockSize"] = value["block_size"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChangedBlocksResponse:
    out: ListChangedBlocksResponse = {}  # type: ignore[typeddict-item]
    if "ChangedBlocks" in data:
        import aws_sdk_ebs.types.changed_blocks

        out["changed_blocks"] = aws_sdk_ebs.types.changed_blocks.deserialize_json(
            data["ChangedBlocks"]
        )
    if "ExpiryTime" in data:
        import aws_sdk_ebs.types.time_stamp

        out["expiry_time"] = aws_sdk_ebs.types.time_stamp.deserialize_json(
            data["ExpiryTime"]
        )
    if "VolumeSize" in data:
        out["volume_size"] = data["VolumeSize"]
    if "BlockSize" in data:
        out["block_size"] = data["BlockSize"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
