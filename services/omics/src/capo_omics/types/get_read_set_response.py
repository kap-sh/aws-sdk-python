"""Generated from Smithy shape ``com.amazonaws.omics#GetReadSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.read_set_streaming_blob


class GetReadSetResponse(TypedDict, closed=True):
    payload: "capo_omics.types.read_set_streaming_blob.ReadSetStreamingBlob"
    """<p>The read set file payload.</p>"""
