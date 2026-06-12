"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateJourneyStateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.journey_state_request


class UpdateJourneyStateRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    journey_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the journey.</p>"""
    journey_state_request: NotRequired[
        "aws_sdk_pinpoint.types.journey_state_request.JourneyStateRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateJourneyStateRequest) -> dict:
    out: dict = {}
    if "journey_state_request" in value:
        import aws_sdk_pinpoint.types.journey_state_request

        out["JourneyStateRequest"] = (
            aws_sdk_pinpoint.types.journey_state_request.serialize_json(
                value["journey_state_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateJourneyStateRequest:
    out: UpdateJourneyStateRequest = {}  # type: ignore[typeddict-item]
    if "JourneyStateRequest" in data:
        import aws_sdk_pinpoint.types.journey_state_request

        out["journey_state_request"] = (
            aws_sdk_pinpoint.types.journey_state_request.deserialize_json(
                data["JourneyStateRequest"]
            )
        )
    return out
