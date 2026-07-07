"""Generated from Smithy shape ``com.amazonaws.wisdom#RemoveKnowledgeBaseTemplateUriRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.uuid_or_arn


class RemoveKnowledgeBaseTemplateUriRequest(TypedDict, closed=True):
    knowledge_base_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveKnowledgeBaseTemplateUriRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveKnowledgeBaseTemplateUriRequest:
    out: RemoveKnowledgeBaseTemplateUriRequest = {}  # type: ignore[typeddict-item]
    return out
