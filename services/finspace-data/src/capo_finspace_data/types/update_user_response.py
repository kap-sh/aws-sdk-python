"""Generated from Smithy shape ``com.amazonaws.finspacedata#UpdateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.user_id


class UpdateUserResponse(TypedDict, closed=True):
    user_id: NotRequired["capo_finspace_data.types.user_id.UserId"]
    """<p>The unique identifier of the updated user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserResponse) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> UpdateUserResponse:
    out: UpdateUserResponse = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    return out
