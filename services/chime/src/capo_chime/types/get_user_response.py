"""Generated from Smithy shape ``com.amazonaws.chime#GetUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.user


class GetUserResponse(TypedDict, closed=True):
    user: NotRequired["capo_chime.types.user.User"]
    """<p>The user details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import capo_chime.types.user

        out["User"] = capo_chime.types.user.serialize_json(value["user"])
    return out


def deserialize_json(data: dict) -> GetUserResponse:
    out: GetUserResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import capo_chime.types.user

        out["user"] = capo_chime.types.user.deserialize_json(data["User"])
    return out
