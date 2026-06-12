"""Generated from Smithy shape ``com.amazonaws.pinpoint#PutEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.events_response


class PutEventsResponse(TypedDict):
    events_response: NotRequired[
        "aws_sdk_pinpoint.types.events_response.EventsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PutEventsResponse) -> dict:
    out: dict = {}
    if "events_response" in value:
        import aws_sdk_pinpoint.types.events_response

        out["EventsResponse"] = aws_sdk_pinpoint.types.events_response.serialize_json(
            value["events_response"]
        )
    return out


def deserialize_json(data: dict) -> PutEventsResponse:
    out: PutEventsResponse = {}  # type: ignore[typeddict-item]
    if "EventsResponse" in data:
        import aws_sdk_pinpoint.types.events_response

        out["events_response"] = (
            aws_sdk_pinpoint.types.events_response.deserialize_json(
                data["EventsResponse"]
            )
        )
    return out
