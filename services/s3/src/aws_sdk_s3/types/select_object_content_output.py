"""Generated from Smithy shape ``com.amazonaws.s3#SelectObjectContentOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3.types.select_object_content_event_stream


class SelectObjectContentOutput(TypedDict):
    payload: NotRequired[
        "aws_sdk_s3.types.select_object_content_event_stream.SelectObjectContentEventStream"
    ]
    """<p>The array of results.</p>"""
