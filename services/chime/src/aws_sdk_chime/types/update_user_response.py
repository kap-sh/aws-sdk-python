"""Generated from Smithy shape ``com.amazonaws.chime#UpdateUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.user


class UpdateUserResponse(TypedDict):
    user: NotRequired["aws_sdk_chime.types.user.User"]
    """<p>The updated user details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import aws_sdk_chime.types.user

        out["User"] = aws_sdk_chime.types.user.serialize_json(value["user"])
    return out


def deserialize_json(data: dict) -> UpdateUserResponse:
    out: UpdateUserResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import aws_sdk_chime.types.user

        out["user"] = aws_sdk_chime.types.user.deserialize_json(data["User"])
    return out
