"""Generated from Smithy shape ``com.amazonaws.transfer#StartRemoteMoveResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.move_id


class StartRemoteMoveResponse(TypedDict, closed=True):
    move_id: "aws_sdk_transfer.types.move_id.MoveId"
    """<p>Returns a unique identifier for the move/rename operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRemoteMoveResponse) -> dict:
    out: dict = {}
    out["MoveId"] = value["move_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRemoteMoveResponse:
    out: StartRemoteMoveResponse = {}  # type: ignore[typeddict-item]
    if "MoveId" in data:
        out["move_id"] = data["MoveId"]
    else:
        raise DeserializationError("StartRemoteMoveResponse.move_id required")
    return out
