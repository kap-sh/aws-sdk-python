"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateJourneyStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.journey_state_request


class UpdateJourneyStateRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    journey_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the journey.</p>"""
    journey_state_request: NotRequired[
        "capo_pinpoint.types.journey_state_request.JourneyStateRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateJourneyStateRequest) -> dict:
    out: dict = {}
    if "journey_state_request" in value:
        import capo_pinpoint.types.journey_state_request

        out["JourneyStateRequest"] = (
            capo_pinpoint.types.journey_state_request.serialize_json(
                value["journey_state_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateJourneyStateRequest:
    out: UpdateJourneyStateRequest = {}  # type: ignore[typeddict-item]
    if "JourneyStateRequest" in data:
        import capo_pinpoint.types.journey_state_request

        out["journey_state_request"] = (
            capo_pinpoint.types.journey_state_request.deserialize_json(
                data["JourneyStateRequest"]
            )
        )
    return out
