"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetJourneyRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.journey_runs_response


class GetJourneyRunsResponse(TypedDict, closed=True):
    journey_runs_response: NotRequired[
        "capo_pinpoint.types.journey_runs_response.JourneyRunsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetJourneyRunsResponse) -> dict:
    out: dict = {}
    if "journey_runs_response" in value:
        import capo_pinpoint.types.journey_runs_response

        out["JourneyRunsResponse"] = (
            capo_pinpoint.types.journey_runs_response.serialize_json(
                value["journey_runs_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetJourneyRunsResponse:
    out: GetJourneyRunsResponse = {}  # type: ignore[typeddict-item]
    if "JourneyRunsResponse" in data:
        import capo_pinpoint.types.journey_runs_response

        out["journey_runs_response"] = (
            capo_pinpoint.types.journey_runs_response.deserialize_json(
                data["JourneyRunsResponse"]
            )
        )
    return out
