"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogObjectResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.get_log_object_response_stream


class GetLogObjectResponse(TypedDict):
    field_stream: NotRequired[
        "aws_sdk_cloudwatch_logs.types.get_log_object_response_stream.GetLogObjectResponseStream"
    ]
    """<p>A stream of structured log data returned by the GetLogObject operation. This stream contains log events with their associated metadata and extracted fields.</p>"""
