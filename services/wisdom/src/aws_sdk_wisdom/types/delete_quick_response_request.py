"""Generated from Smithy shape ``com.amazonaws.wisdom#DeleteQuickResponseRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.uuid_or_arn


class DeleteQuickResponseRequest(TypedDict):
    knowledge_base_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The knowledge base from which the quick response is deleted. The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.</p>"""
    quick_response_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the quick response to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQuickResponseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQuickResponseRequest:
    out: DeleteQuickResponseRequest = {}  # type: ignore[typeddict-item]
    return out
