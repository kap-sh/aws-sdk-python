"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteJourneyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.journey_response


class DeleteJourneyResponse(TypedDict):
    journey_response: NotRequired[
        "aws_sdk_pinpoint.types.journey_response.JourneyResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteJourneyResponse) -> dict:
    out: dict = {}
    if "journey_response" in value:
        import aws_sdk_pinpoint.types.journey_response

        out["JourneyResponse"] = aws_sdk_pinpoint.types.journey_response.serialize_json(
            value["journey_response"]
        )
    return out


def deserialize_json(data: dict) -> DeleteJourneyResponse:
    out: DeleteJourneyResponse = {}  # type: ignore[typeddict-item]
    if "JourneyResponse" in data:
        import aws_sdk_pinpoint.types.journey_response

        out["journey_response"] = (
            aws_sdk_pinpoint.types.journey_response.deserialize_json(
                data["JourneyResponse"]
            )
        )
    return out
