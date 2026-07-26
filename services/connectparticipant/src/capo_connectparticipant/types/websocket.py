"""Generated from Smithy shape ``com.amazonaws.connectparticipant#Websocket``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.iso8601_datetime
    import capo_connectparticipant.types.pre_signed_connection_url


class Websocket(TypedDict, closed=True):
    url: NotRequired[
        "capo_connectparticipant.types.pre_signed_connection_url.PreSignedConnectionUrl"
    ]
    """<p>The URL of the websocket.</p>"""
    connection_expiry: NotRequired[
        "capo_connectparticipant.types.iso8601_datetime.ISO8601Datetime"
    ]
    """<p>The URL expiration timestamp in ISO date format.</p> <p>It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Websocket) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    if "connection_expiry" in value:
        out["ConnectionExpiry"] = value["connection_expiry"]
    return out


def deserialize_json(data: dict) -> Websocket:
    out: Websocket = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    if "ConnectionExpiry" in data:
        out["connection_expiry"] = data["ConnectionExpiry"]
    return out
