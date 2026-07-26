"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateJourneyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.write_journey_request


class UpdateJourneyRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    journey_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the journey.</p>"""
    write_journey_request: NotRequired[
        "capo_pinpoint.types.write_journey_request.WriteJourneyRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateJourneyRequest) -> dict:
    out: dict = {}
    if "write_journey_request" in value:
        import capo_pinpoint.types.write_journey_request

        out["WriteJourneyRequest"] = (
            capo_pinpoint.types.write_journey_request.serialize_json(
                value["write_journey_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateJourneyRequest:
    out: UpdateJourneyRequest = {}  # type: ignore[typeddict-item]
    if "WriteJourneyRequest" in data:
        import capo_pinpoint.types.write_journey_request

        out["write_journey_request"] = (
            capo_pinpoint.types.write_journey_request.deserialize_json(
                data["WriteJourneyRequest"]
            )
        )
    return out
