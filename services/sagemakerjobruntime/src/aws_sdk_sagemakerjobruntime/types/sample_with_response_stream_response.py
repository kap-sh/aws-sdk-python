"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#SampleWithResponseStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemakerjobruntime.types.response_stream


class SampleWithResponseStreamResponse(TypedDict, closed=True):
    content_type: NotRequired["str"]
    """MIME type of the streaming inference result."""
    body: "aws_sdk_sagemakerjobruntime.types.response_stream.ResponseStream"
    """The streaming response body, delivered as a series of PayloadPart events."""
