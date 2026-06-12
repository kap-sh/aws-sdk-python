"""Generated from Smithy shape ``com.amazonaws.pinpoint#ItemResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.endpoint_item_response
    import aws_sdk_pinpoint.types.map_of_event_item_response


class ItemResponse(TypedDict):
    endpoint_item_response: NotRequired[
        "aws_sdk_pinpoint.types.endpoint_item_response.EndpointItemResponse"
    ]
    """<p>The response that was received after the endpoint data was accepted.</p>"""
    events_item_response: NotRequired[
        "aws_sdk_pinpoint.types.map_of_event_item_response.MapOfEventItemResponse"
    ]
    """<p>A multipart response object that contains a key and a value for each event in the request. In each object, the event ID is the key and an EventItemResponse object is the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ItemResponse) -> dict:
    out: dict = {}
    if "endpoint_item_response" in value:
        import aws_sdk_pinpoint.types.endpoint_item_response

        out["EndpointItemResponse"] = (
            aws_sdk_pinpoint.types.endpoint_item_response.serialize_json(
                value["endpoint_item_response"]
            )
        )
    if "events_item_response" in value:
        import aws_sdk_pinpoint.types.map_of_event_item_response

        out["EventsItemResponse"] = (
            aws_sdk_pinpoint.types.map_of_event_item_response.serialize_json(
                value["events_item_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> ItemResponse:
    out: ItemResponse = {}  # type: ignore[typeddict-item]
    if "EndpointItemResponse" in data:
        import aws_sdk_pinpoint.types.endpoint_item_response

        out["endpoint_item_response"] = (
            aws_sdk_pinpoint.types.endpoint_item_response.deserialize_json(
                data["EndpointItemResponse"]
            )
        )
    if "EventsItemResponse" in data:
        import aws_sdk_pinpoint.types.map_of_event_item_response

        out["events_item_response"] = (
            aws_sdk_pinpoint.types.map_of_event_item_response.deserialize_json(
                data["EventsItemResponse"]
            )
        )
    return out
