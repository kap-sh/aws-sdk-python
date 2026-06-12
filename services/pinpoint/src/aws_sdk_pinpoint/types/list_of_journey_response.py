"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfJourneyResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.journey_response

ListOfJourneyResponse: TypeAlias = list[
    "aws_sdk_pinpoint.types.journey_response.JourneyResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfJourneyResponse) -> list:
    import aws_sdk_pinpoint.types.journey_response

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.journey_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfJourneyResponse:
    import aws_sdk_pinpoint.types.journey_response

    out: ListOfJourneyResponse = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.journey_response.deserialize_json(item))
    return out
