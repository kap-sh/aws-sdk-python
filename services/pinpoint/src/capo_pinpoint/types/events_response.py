"""Generated from Smithy shape ``com.amazonaws.pinpoint#EventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.map_of_item_response


class EventsResponse(TypedDict, closed=True):
    results: NotRequired["capo_pinpoint.types.map_of_item_response.MapOfItemResponse"]
    """<p>A map that contains a multipart response for each endpoint. For each item in this object, the endpoint ID is the key and the item response is the value. If no item response exists, the value can also be one of the following: 202, the request was processed successfully; or 400, the payload wasn't valid or required fields were missing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventsResponse) -> dict:
    out: dict = {}
    if "results" in value:
        import capo_pinpoint.types.map_of_item_response

        out["Results"] = capo_pinpoint.types.map_of_item_response.serialize_json(
            value["results"]
        )
    return out


def deserialize_json(data: dict) -> EventsResponse:
    out: EventsResponse = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import capo_pinpoint.types.map_of_item_response

        out["results"] = capo_pinpoint.types.map_of_item_response.deserialize_json(
            data["Results"]
        )
    return out
