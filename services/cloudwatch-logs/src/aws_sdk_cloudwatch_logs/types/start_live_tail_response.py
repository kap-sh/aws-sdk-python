"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StartLiveTailResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.start_live_tail_response_stream


class StartLiveTailResponse(TypedDict):
    response_stream: NotRequired[
        "aws_sdk_cloudwatch_logs.types.start_live_tail_response_stream.StartLiveTailResponseStream"
    ]
    """<p>An object that includes the stream returned by your request. It can include both log events and exceptions.</p>"""
