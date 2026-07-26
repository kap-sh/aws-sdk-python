"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfJourneyRunResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.journey_run_response

ListOfJourneyRunResponse: TypeAlias = list[
    "capo_pinpoint.types.journey_run_response.JourneyRunResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfJourneyRunResponse) -> list:
    import capo_pinpoint.types.journey_run_response

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.journey_run_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfJourneyRunResponse:
    import capo_pinpoint.types.journey_run_response

    out: ListOfJourneyRunResponse = []
    for item in data:
        out.append(capo_pinpoint.types.journey_run_response.deserialize_json(item))
    return out
