"""Generated from Smithy shape ``com.amazonaws.bedrock#GetCustomModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.model_identifier


class GetCustomModelRequest(TypedDict, closed=True):
    model_identifier: "capo_bedrock.types.model_identifier.ModelIdentifier"
    """<p>Name or Amazon Resource Name (ARN) of the custom model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCustomModelRequest:
    out: GetCustomModelRequest = {}  # type: ignore[typeddict-item]
    return out
