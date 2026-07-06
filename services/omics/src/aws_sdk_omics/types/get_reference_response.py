"""Generated from Smithy shape ``com.amazonaws.omics#GetReferenceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.reference_streaming_blob


class GetReferenceResponse(TypedDict, closed=True):
    payload: "aws_sdk_omics.types.reference_streaming_blob.ReferenceStreamingBlob"
    """<p>The reference file payload.</p>"""
