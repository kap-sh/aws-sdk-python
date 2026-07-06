"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecuteActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class ExecuteActionResponse(TypedDict, closed=True):
    action_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteActionResponse) -> dict:
    out: dict = {}
    out["actionId"] = value["action_id"]
    return out


def deserialize_json(data: dict) -> ExecuteActionResponse:
    out: ExecuteActionResponse = {}  # type: ignore[typeddict-item]
    if "actionId" in data:
        out["action_id"] = data["actionId"]
    else:
        raise DeserializationError("ExecuteActionResponse.action_id required")
    return out
