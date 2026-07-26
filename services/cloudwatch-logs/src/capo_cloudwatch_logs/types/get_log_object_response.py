"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogObjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.get_log_object_response_stream


class GetLogObjectResponse(TypedDict, closed=True):
    field_stream: NotRequired[
        "capo_cloudwatch_logs.types.get_log_object_response_stream.GetLogObjectResponseStream"
    ]
    """<p>A stream of structured log data returned by the GetLogObject operation. This stream contains log events with their associated metadata and extracted fields.</p>"""
