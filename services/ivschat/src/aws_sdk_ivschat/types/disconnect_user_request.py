"""Generated from Smithy shape ``com.amazonaws.ivschat#DisconnectUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivschat.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.reason
    import aws_sdk_ivschat.types.room_identifier
    import aws_sdk_ivschat.types.user_id


class DisconnectUserRequest(TypedDict, closed=True):
    room_identifier: "aws_sdk_ivschat.types.room_identifier.RoomIdentifier"
    """<p>Identifier of the room from which the user's clients should be disconnected. Currently this must be an ARN.</p>"""
    user_id: "aws_sdk_ivschat.types.user_id.UserID"
    """<p>ID of the user (connection) to disconnect from the room.</p>"""
    reason: NotRequired["aws_sdk_ivschat.types.reason.Reason"]
    """<p>Reason for disconnecting the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectUserRequest) -> dict:
    out: dict = {}
    out["roomIdentifier"] = value["room_identifier"]
    out["userId"] = value["user_id"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> DisconnectUserRequest:
    out: DisconnectUserRequest = {}  # type: ignore[typeddict-item]
    if "roomIdentifier" in data:
        out["room_identifier"] = data["roomIdentifier"]
    else:
        raise DeserializationError("DisconnectUserRequest.room_identifier required")
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("DisconnectUserRequest.user_id required")
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
