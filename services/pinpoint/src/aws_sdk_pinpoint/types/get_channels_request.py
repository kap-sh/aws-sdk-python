"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetChannelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class GetChannelsRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetChannelsRequest:
    out: GetChannelsRequest = {}  # type: ignore[typeddict-item]
    return out
