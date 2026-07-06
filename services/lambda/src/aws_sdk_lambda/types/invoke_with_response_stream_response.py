"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeWithResponseStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.integer
    import aws_sdk_lambda.types.invoke_with_response_stream_response_event
    import aws_sdk_lambda.types.string
    import aws_sdk_lambda.types.version


class InvokeWithResponseStreamResponse(TypedDict, closed=True):
    status_code: "aws_sdk_lambda.types.integer.Integer"
    """<p>For a successful request, the HTTP status code is in the 200 range. For the <code>RequestResponse</code> invocation type, this status code is 200. For the <code>DryRun</code> invocation type, this status code is 204.</p>"""
    executed_version: NotRequired["aws_sdk_lambda.types.version.Version"]
    """<p>The version of the function that executed. When you invoke a function with an alias, this indicates which version the alias resolved to.</p>"""
    event_stream: NotRequired[
        "aws_sdk_lambda.types.invoke_with_response_stream_response_event.InvokeWithResponseStreamResponseEvent"
    ]
    """<p>The stream of response payloads.</p>"""
    response_stream_content_type: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The type of data the stream is returning.</p>"""
