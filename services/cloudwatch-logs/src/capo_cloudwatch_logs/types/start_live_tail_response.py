"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StartLiveTailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.start_live_tail_response_stream


class StartLiveTailResponse(TypedDict, closed=True):
    response_stream: NotRequired[
        "capo_cloudwatch_logs.types.start_live_tail_response_stream.StartLiveTailResponseStream"
    ]
    """<p>An object that includes the stream returned by your request. It can include both log events and exceptions.</p>"""
