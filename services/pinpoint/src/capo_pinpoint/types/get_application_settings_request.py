"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetApplicationSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string


class GetApplicationSettingsRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetApplicationSettingsRequest:
    out: GetApplicationSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
