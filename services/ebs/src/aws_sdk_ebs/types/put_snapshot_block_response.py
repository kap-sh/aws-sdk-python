"""Generated from Smithy shape ``com.amazonaws.ebs#PutSnapshotBlockResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ebs.types.checksum
    import aws_sdk_ebs.types.checksum_algorithm


class PutSnapshotBlockResponse(TypedDict, closed=True):
    checksum: NotRequired["aws_sdk_ebs.types.checksum.Checksum"]
    """<p>The SHA256 checksum generated for the block data by Amazon EBS.</p>"""
    checksum_algorithm: NotRequired[
        "aws_sdk_ebs.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>The algorithm used by Amazon EBS to generate the checksum.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSnapshotBlockResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutSnapshotBlockResponse:
    out: PutSnapshotBlockResponse = {}  # type: ignore[typeddict-item]
    return out
