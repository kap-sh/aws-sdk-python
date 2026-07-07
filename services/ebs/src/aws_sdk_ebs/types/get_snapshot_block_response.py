"""Generated from Smithy shape ``com.amazonaws.ebs#GetSnapshotBlockResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ebs.types.block_data
    import aws_sdk_ebs.types.checksum
    import aws_sdk_ebs.types.checksum_algorithm
    import aws_sdk_ebs.types.data_length


class GetSnapshotBlockResponse(TypedDict, closed=True):
    data_length: NotRequired["aws_sdk_ebs.types.data_length.DataLength"]
    """<p>The size of the data in the block.</p>"""
    block_data: "aws_sdk_ebs.types.block_data.BlockData"
    """<p>The data content of the block.</p>"""
    checksum: NotRequired["aws_sdk_ebs.types.checksum.Checksum"]
    """<p>The checksum generated for the block, which is Base64 encoded.</p>"""
    checksum_algorithm: NotRequired[
        "aws_sdk_ebs.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>The algorithm used to generate the checksum for the block, such as SHA256.</p>"""
