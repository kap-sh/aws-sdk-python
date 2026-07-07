"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateJourneyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.journey_response


class UpdateJourneyResponse(TypedDict, closed=True):
    journey_response: NotRequired[
        "aws_sdk_pinpoint.types.journey_response.JourneyResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateJourneyResponse) -> dict:
    out: dict = {}
    if "journey_response" in value:
        import aws_sdk_pinpoint.types.journey_response

        out["JourneyResponse"] = aws_sdk_pinpoint.types.journey_response.serialize_json(
            value["journey_response"]
        )
    return out


def deserialize_json(data: dict) -> UpdateJourneyResponse:
    out: UpdateJourneyResponse = {}  # type: ignore[typeddict-item]
    if "JourneyResponse" in data:
        import aws_sdk_pinpoint.types.journey_response

        out["journey_response"] = (
            aws_sdk_pinpoint.types.journey_response.deserialize_json(
                data["JourneyResponse"]
            )
        )
    return out
