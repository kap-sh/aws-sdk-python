"""Generated from Smithy shape ``com.amazonaws.wisdom#GetAssistantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.uuid_or_arn


class GetAssistantRequest(TypedDict, closed=True):
    assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssistantRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssistantRequest:
    out: GetAssistantRequest = {}  # type: ignore[typeddict-item]
    return out
