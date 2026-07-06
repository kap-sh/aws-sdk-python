"""Generated from Smithy shape ``com.amazonaws.ivschat#GetRoomRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ivschat.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.room_identifier


class GetRoomRequest(TypedDict, closed=True):
    identifier: "aws_sdk_ivschat.types.room_identifier.RoomIdentifier"
    """<p>Identifier of the room for which the configuration is to be retrieved. Currently this must be an ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRoomRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> GetRoomRequest:
    out: GetRoomRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("GetRoomRequest.identifier required")
    return out
