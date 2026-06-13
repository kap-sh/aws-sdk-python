"""Generated from Smithy shape ``com.amazonaws.wisdom#DeleteKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.uuid_or_arn


class DeleteKnowledgeBaseRequest(TypedDict):
    knowledge_base_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The knowledge base to delete content from. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKnowledgeBaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKnowledgeBaseRequest:
    out: DeleteKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    return out
