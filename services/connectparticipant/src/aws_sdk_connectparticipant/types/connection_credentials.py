"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ConnectionCredentials``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.iso8601_datetime
    import aws_sdk_connectparticipant.types.participant_token


class ConnectionCredentials(TypedDict):
    connection_token: NotRequired[
        "aws_sdk_connectparticipant.types.participant_token.ParticipantToken"
    ]
    """<p>The connection token.</p>"""
    expiry: NotRequired[
        "aws_sdk_connectparticipant.types.iso8601_datetime.ISO8601Datetime"
    ]
    """<p>The expiration of the token.</p> <p>It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionCredentials) -> dict:
    out: dict = {}
    if "connection_token" in value:
        out["ConnectionToken"] = value["connection_token"]
    if "expiry" in value:
        out["Expiry"] = value["expiry"]
    return out


def deserialize_json(data: dict) -> ConnectionCredentials:
    out: ConnectionCredentials = {}  # type: ignore[typeddict-item]
    if "ConnectionToken" in data:
        out["connection_token"] = data["ConnectionToken"]
    if "Expiry" in data:
        out["expiry"] = data["Expiry"]
    return out
