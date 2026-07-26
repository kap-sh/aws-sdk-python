"""Generated from Smithy shape ``com.amazonaws.wisdom#GetContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.uuid_or_arn


class GetContentRequest(TypedDict, closed=True):
    content_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetContentRequest:
    out: GetContentRequest = {}  # type: ignore[typeddict-item]
    return out
