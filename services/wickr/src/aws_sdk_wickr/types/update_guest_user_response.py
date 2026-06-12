"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateGuestUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class UpdateGuestUserResponse(TypedDict):
    message: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A message indicating the result of the update operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGuestUserResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UpdateGuestUserResponse:
    out: UpdateGuestUserResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out
