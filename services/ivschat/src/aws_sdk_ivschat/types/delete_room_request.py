"""Generated from Smithy shape ``com.amazonaws.ivschat#DeleteRoomRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivschat.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.room_identifier


class DeleteRoomRequest(TypedDict):
    identifier: "aws_sdk_ivschat.types.room_identifier.RoomIdentifier"
    """<p>Identifier of the room to be deleted. Currently this must be an ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRoomRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> DeleteRoomRequest:
    out: DeleteRoomRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("DeleteRoomRequest.identifier required")
    return out
