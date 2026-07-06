"""Generated from Smithy shape ``com.amazonaws.qconnect#ListMessagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.max_results
    import aws_sdk_qconnect.types.message_filter_type
    import aws_sdk_qconnect.types.next_token
    import aws_sdk_qconnect.types.uuid_or_arn


class ListMessagesRequest(TypedDict, closed=True):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant.</p>"""
    session_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect session.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_qconnect.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    filter: NotRequired["aws_sdk_qconnect.types.message_filter_type.MessageFilterType"]
    """<p>The filter criteria for listing messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMessagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMessagesRequest:
    out: ListMessagesRequest = {}  # type: ignore[typeddict-item]
    return out
