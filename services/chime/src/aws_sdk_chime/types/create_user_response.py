"""Generated from Smithy shape ``com.amazonaws.chime#CreateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.user


class CreateUserResponse(TypedDict, closed=True):
    user: NotRequired["aws_sdk_chime.types.user.User"]
    """<p>The user on the Amazon Chime account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import aws_sdk_chime.types.user

        out["User"] = aws_sdk_chime.types.user.serialize_json(value["user"])
    return out


def deserialize_json(data: dict) -> CreateUserResponse:
    out: CreateUserResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import aws_sdk_chime.types.user

        out["user"] = aws_sdk_chime.types.user.deserialize_json(data["User"])
    return out
