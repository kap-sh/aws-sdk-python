"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateGuestUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class UpdateGuestUserResponse(TypedDict, closed=True):
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
