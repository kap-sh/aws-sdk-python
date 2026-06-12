"""Generated from Smithy shape ``com.amazonaws.finspacedata#DisableUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.user_id


class DisableUserResponse(TypedDict):
    user_id: NotRequired["aws_sdk_finspace_data.types.user_id.UserId"]
    """<p>The unique identifier for the deactivated user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableUserResponse) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> DisableUserResponse:
    out: DisableUserResponse = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    return out
