"""Generated from Smithy shape ``com.amazonaws.omics#GetReadSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.read_set_streaming_blob


class GetReadSetResponse(TypedDict):
    payload: "aws_sdk_omics.types.read_set_streaming_blob.ReadSetStreamingBlob"
    """<p>The read set file payload.</p>"""
