"""Generated from Smithy shape ``com.amazonaws.medialive#ListMultiplexAlertsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_multiplex_alert
    import capo_medialive.types.__string


class ListMultiplexAlertsResponse(TypedDict, closed=True):
    alerts: NotRequired[
        "capo_medialive.types.__list_of_multiplex_alert.__listOfMultiplexAlert"
    ]
    """The alerts found for this multiplex"""
    next_token: NotRequired["capo_medialive.types.__string.__string"]
    """The token to use to retrieve the next page of results"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMultiplexAlertsResponse) -> dict:
    out: dict = {}
    if "alerts" in value:
        import capo_medialive.types.__list_of_multiplex_alert

        out["alerts"] = capo_medialive.types.__list_of_multiplex_alert.serialize_json(
            value["alerts"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMultiplexAlertsResponse:
    out: ListMultiplexAlertsResponse = {}  # type: ignore[typeddict-item]
    if "alerts" in data:
        import capo_medialive.types.__list_of_multiplex_alert

        out["alerts"] = capo_medialive.types.__list_of_multiplex_alert.deserialize_json(
            data["alerts"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
