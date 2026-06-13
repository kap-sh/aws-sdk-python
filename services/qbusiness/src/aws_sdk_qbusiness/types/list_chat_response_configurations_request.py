"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListChatResponseConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.integer
    import aws_sdk_qbusiness.types.next_token


class ListChatResponseConfigurationsRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application for which to list available chat response configurations.</p>"""
    max_results: NotRequired["aws_sdk_qbusiness.types.integer.Integer"]
    """<p>The maximum number of chat response configurations to return in a single response. This parameter helps control pagination of results when many configurations exist.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>A pagination token used to retrieve the next set of results when the number of configurations exceeds the specified <code>maxResults</code> value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChatResponseConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChatResponseConfigurationsRequest:
    out: ListChatResponseConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
