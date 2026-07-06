"""Generated from Smithy shape ``com.amazonaws.wickr#CreateDataRetentionBotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class CreateDataRetentionBotResponse(TypedDict, closed=True):
    message: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A message indicating that the data retention bot was successfully provisioned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataRetentionBotResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CreateDataRetentionBotResponse:
    out: CreateDataRetentionBotResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out
