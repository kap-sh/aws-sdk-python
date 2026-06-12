"""Generated from Smithy shape ``com.amazonaws.workdocs#ActivateUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.user


class ActivateUserResponse(TypedDict):
    user: NotRequired["aws_sdk_workdocs.types.user.User"]
    """<p>The user information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivateUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import aws_sdk_workdocs.types.user

        out["User"] = aws_sdk_workdocs.types.user.serialize_json(value["user"])
    return out


def deserialize_json(data: dict) -> ActivateUserResponse:
    out: ActivateUserResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import aws_sdk_workdocs.types.user

        out["user"] = aws_sdk_workdocs.types.user.deserialize_json(data["User"])
    return out
