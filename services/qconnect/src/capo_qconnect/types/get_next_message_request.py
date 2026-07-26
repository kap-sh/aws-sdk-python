"""Generated from Smithy shape ``com.amazonaws.qconnect#GetNextMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.next_token
    import capo_qconnect.types.uuid_or_arn


class GetNextMessageRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant.</p>"""
    session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect session.</p>"""
    next_message_token: "capo_qconnect.types.next_token.NextToken"
    """<p>The token for the next message. Use the value returned in the SendMessage or previous response in the next request to retrieve the next message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNextMessageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNextMessageRequest:
    out: GetNextMessageRequest = {}  # type: ignore[typeddict-item]
    return out
