"""Generated from Smithy shape ``com.amazonaws.workdocs#GetCurrentUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.user


class GetCurrentUserResponse(TypedDict, closed=True):
    user: NotRequired["aws_sdk_workdocs.types.user.User"]
    """<p>Metadata of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCurrentUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import aws_sdk_workdocs.types.user

        out["User"] = aws_sdk_workdocs.types.user.serialize_json(value["user"])
    return out


def deserialize_json(data: dict) -> GetCurrentUserResponse:
    out: GetCurrentUserResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import aws_sdk_workdocs.types.user

        out["user"] = aws_sdk_workdocs.types.user.deserialize_json(data["User"])
    return out
