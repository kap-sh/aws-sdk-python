"""Generated from Smithy shape ``com.amazonaws.omics#GetReadSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.read_set_file
    import capo_omics.types.read_set_id
    import capo_omics.types.sequence_store_id


class GetReadSetRequest(TypedDict, closed=True):
    id: "capo_omics.types.read_set_id.ReadSetId"
    """<p>The read set's ID.</p>"""
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read set's sequence store ID.</p>"""
    file: NotRequired["capo_omics.types.read_set_file.ReadSetFile"]
    """<p>The file to retrieve.</p>"""
    part_number: "int"
    """<p>The part number to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReadSetRequest:
    out: GetReadSetRequest = {}  # type: ignore[typeddict-item]
    return out
