"""Generated from Smithy shape ``com.amazonaws.workdocs#UpdateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.user


class UpdateUserResponse(TypedDict, closed=True):
    user: NotRequired["capo_workdocs.types.user.User"]
    """<p>The user information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import capo_workdocs.types.user

        out["User"] = capo_workdocs.types.user.serialize_json(value["user"])
    return out


def deserialize_json(data: dict) -> UpdateUserResponse:
    out: UpdateUserResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import capo_workdocs.types.user

        out["user"] = capo_workdocs.types.user.deserialize_json(data["User"])
    return out
