"""Generated from Smithy shape ``com.amazonaws.wickr#DeleteBotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class DeleteBotResponse(TypedDict, closed=True):
    message: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A message indicating the result of the bot deletion operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteBotResponse:
    out: DeleteBotResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out
