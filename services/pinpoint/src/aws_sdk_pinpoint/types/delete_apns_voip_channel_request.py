"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteApnsVoipChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class DeleteApnsVoipChannelRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApnsVoipChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApnsVoipChannelRequest:
    out: DeleteApnsVoipChannelRequest = {}  # type: ignore[typeddict-item]
    return out
