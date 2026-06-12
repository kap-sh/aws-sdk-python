"""Generated from Smithy shape ``com.amazonaws.finspacedata#EnableUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.user_id


class EnableUserResponse(TypedDict):
    user_id: NotRequired["aws_sdk_finspace_data.types.user_id.UserId"]
    """<p>The unique identifier for the active user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableUserResponse) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> EnableUserResponse:
    out: EnableUserResponse = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    return out
