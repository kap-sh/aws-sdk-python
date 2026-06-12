"""Generated from Smithy shape ``com.amazonaws.medialive#ListMultiplexAlertsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_multiplex_alert
    import aws_sdk_medialive.types.__string


class ListMultiplexAlertsResponse(TypedDict):
    alerts: NotRequired[
        "aws_sdk_medialive.types.__list_of_multiplex_alert.__listOfMultiplexAlert"
    ]
    """The alerts found for this multiplex"""
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The token to use to retrieve the next page of results"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMultiplexAlertsResponse) -> dict:
    out: dict = {}
    if "alerts" in value:
        import aws_sdk_medialive.types.__list_of_multiplex_alert

        out["alerts"] = (
            aws_sdk_medialive.types.__list_of_multiplex_alert.serialize_json(
                value["alerts"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMultiplexAlertsResponse:
    out: ListMultiplexAlertsResponse = {}  # type: ignore[typeddict-item]
    if "alerts" in data:
        import aws_sdk_medialive.types.__list_of_multiplex_alert

        out["alerts"] = (
            aws_sdk_medialive.types.__list_of_multiplex_alert.deserialize_json(
                data["alerts"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
