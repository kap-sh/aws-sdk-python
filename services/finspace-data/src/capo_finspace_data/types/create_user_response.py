"""Generated from Smithy shape ``com.amazonaws.finspacedata#CreateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.user_id


class CreateUserResponse(TypedDict, closed=True):
    user_id: NotRequired["capo_finspace_data.types.user_id.UserId"]
    """<p>The unique identifier for the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserResponse) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> CreateUserResponse:
    out: CreateUserResponse = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    return out
