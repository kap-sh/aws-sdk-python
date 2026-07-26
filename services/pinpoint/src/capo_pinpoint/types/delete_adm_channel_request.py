"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteAdmChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string


class DeleteAdmChannelRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAdmChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAdmChannelRequest:
    out: DeleteAdmChannelRequest = {}  # type: ignore[typeddict-item]
    return out
