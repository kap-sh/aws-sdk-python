"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetApnsVoipChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class GetApnsVoipChannelRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApnsVoipChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApnsVoipChannelRequest:
    out: GetApnsVoipChannelRequest = {}  # type: ignore[typeddict-item]
    return out
