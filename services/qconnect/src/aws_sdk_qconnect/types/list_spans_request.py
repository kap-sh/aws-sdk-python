"""Generated from Smithy shape ``com.amazonaws.qconnect#ListSpansRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.max_results
    import aws_sdk_qconnect.types.next_token
    import aws_sdk_qconnect.types.uuid_or_arn


class ListSpansRequest(TypedDict, closed=True):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>UUID or ARN of the Connect AI Assistant resource</p>"""
    session_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>UUID or ARN of the Connect AI Session resource</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>Pagination token for retrieving the next page of results</p>"""
    max_results: NotRequired["aws_sdk_qconnect.types.max_results.MaxResults"]
    """<p>Maximum number of spans to return per page</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSpansRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSpansRequest:
    out: ListSpansRequest = {}  # type: ignore[typeddict-item]
    return out
