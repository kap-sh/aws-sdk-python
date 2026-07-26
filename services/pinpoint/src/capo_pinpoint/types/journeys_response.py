"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.list_of_journey_response


class JourneysResponse(TypedDict, closed=True):
    item: NotRequired[
        "capo_pinpoint.types.list_of_journey_response.ListOfJourneyResponse"
    ]
    """<p>An array of responses, one for each journey that's associated with the application.</p>"""
    next_token: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneysResponse) -> dict:
    out: dict = {}
    if "item" in value:
        import capo_pinpoint.types.list_of_journey_response

        out["Item"] = capo_pinpoint.types.list_of_journey_response.serialize_json(
            value["item"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> JourneysResponse:
    out: JourneysResponse = {}  # type: ignore[typeddict-item]
    if "Item" in data:
        import capo_pinpoint.types.list_of_journey_response

        out["item"] = capo_pinpoint.types.list_of_journey_response.deserialize_json(
            data["Item"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
