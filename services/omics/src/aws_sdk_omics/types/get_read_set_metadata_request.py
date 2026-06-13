"""Generated from Smithy shape ``com.amazonaws.omics#GetReadSetMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.read_set_id
    import aws_sdk_omics.types.sequence_store_id


class GetReadSetMetadataRequest(TypedDict):
    id: "aws_sdk_omics.types.read_set_id.ReadSetId"
    """<p>The read set's ID.</p>"""
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read set's sequence store ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadSetMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReadSetMetadataRequest:
    out: GetReadSetMetadataRequest = {}  # type: ignore[typeddict-item]
    return out
