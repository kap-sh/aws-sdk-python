"""Generated from Smithy shape ``com.amazonaws.medialive#ListAlertsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_channel_alert
    import aws_sdk_medialive.types.__string


class ListAlertsResponse(TypedDict, closed=True):
    alerts: NotRequired[
        "aws_sdk_medialive.types.__list_of_channel_alert.__listOfChannelAlert"
    ]
    """The alerts found for this channel"""
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The token to use to retrieve the next page of results"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAlertsResponse) -> dict:
    out: dict = {}
    if "alerts" in value:
        import aws_sdk_medialive.types.__list_of_channel_alert

        out["alerts"] = aws_sdk_medialive.types.__list_of_channel_alert.serialize_json(
            value["alerts"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAlertsResponse:
    out: ListAlertsResponse = {}  # type: ignore[typeddict-item]
    if "alerts" in data:
        import aws_sdk_medialive.types.__list_of_channel_alert

        out["alerts"] = (
            aws_sdk_medialive.types.__list_of_channel_alert.deserialize_json(
                data["alerts"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
