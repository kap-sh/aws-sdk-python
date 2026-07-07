"""Generated from Smithy shape ``com.amazonaws.pinpoint#PutEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.events_request


class PutEventsRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    events_request: NotRequired["aws_sdk_pinpoint.types.events_request.EventsRequest"]


# --- restJson1 ser/de ---
def serialize_json(value: PutEventsRequest) -> dict:
    out: dict = {}
    if "events_request" in value:
        import aws_sdk_pinpoint.types.events_request

        out["EventsRequest"] = aws_sdk_pinpoint.types.events_request.serialize_json(
            value["events_request"]
        )
    return out


def deserialize_json(data: dict) -> PutEventsRequest:
    out: PutEventsRequest = {}  # type: ignore[typeddict-item]
    if "EventsRequest" in data:
        import aws_sdk_pinpoint.types.events_request

        out["events_request"] = aws_sdk_pinpoint.types.events_request.deserialize_json(
            data["EventsRequest"]
        )
    return out
