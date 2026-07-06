"""Generated from Smithy shape ``com.amazonaws.sesv2#GetMessageInsightsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.outbound_message_id


class GetMessageInsightsRequest(TypedDict, closed=True):
    message_id: "aws_sdk_sesv2.types.outbound_message_id.OutboundMessageId"
    """<p> A <code>MessageId</code> is a unique identifier for a message, and is returned when sending emails through Amazon SES. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMessageInsightsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMessageInsightsRequest:
    out: GetMessageInsightsRequest = {}  # type: ignore[typeddict-item]
    return out
