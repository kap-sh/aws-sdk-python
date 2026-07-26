"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetJourneyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string


class GetJourneyRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    journey_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the journey.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJourneyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetJourneyRequest:
    out: GetJourneyRequest = {}  # type: ignore[typeddict-item]
    return out
