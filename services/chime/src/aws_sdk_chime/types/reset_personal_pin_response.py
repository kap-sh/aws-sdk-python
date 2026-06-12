"""Generated from Smithy shape ``com.amazonaws.chime#ResetPersonalPINResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.user


class ResetPersonalPINResponse(TypedDict):
    user: NotRequired["aws_sdk_chime.types.user.User"]
    """<p>The user details and new personal meeting PIN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetPersonalPINResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import aws_sdk_chime.types.user

        out["User"] = aws_sdk_chime.types.user.serialize_json(value["user"])
    return out


def deserialize_json(data: dict) -> ResetPersonalPINResponse:
    out: ResetPersonalPINResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import aws_sdk_chime.types.user

        out["user"] = aws_sdk_chime.types.user.deserialize_json(data["User"])
    return out
