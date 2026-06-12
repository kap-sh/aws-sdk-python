"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfJourneyRunResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.journey_run_response

ListOfJourneyRunResponse: TypeAlias = list[
    "aws_sdk_pinpoint.types.journey_run_response.JourneyRunResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfJourneyRunResponse) -> list:
    import aws_sdk_pinpoint.types.journey_run_response

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.journey_run_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfJourneyRunResponse:
    import aws_sdk_pinpoint.types.journey_run_response

    out: ListOfJourneyRunResponse = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.journey_run_response.deserialize_json(item))
    return out
