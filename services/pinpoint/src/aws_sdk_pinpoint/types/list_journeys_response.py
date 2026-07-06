"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListJourneysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.journeys_response


class ListJourneysResponse(TypedDict, closed=True):
    journeys_response: NotRequired[
        "aws_sdk_pinpoint.types.journeys_response.JourneysResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListJourneysResponse) -> dict:
    out: dict = {}
    if "journeys_response" in value:
        import aws_sdk_pinpoint.types.journeys_response

        out["JourneysResponse"] = (
            aws_sdk_pinpoint.types.journeys_response.serialize_json(
                value["journeys_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListJourneysResponse:
    out: ListJourneysResponse = {}  # type: ignore[typeddict-item]
    if "JourneysResponse" in data:
        import aws_sdk_pinpoint.types.journeys_response

        out["journeys_response"] = (
            aws_sdk_pinpoint.types.journeys_response.deserialize_json(
                data["JourneysResponse"]
            )
        )
    return out
