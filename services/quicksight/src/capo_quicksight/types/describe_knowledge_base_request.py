"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.kb_aws_account_id
    import capo_quicksight.types.knowledge_base_id


class DescribeKnowledgeBaseRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.kb_aws_account_id.KbAwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the knowledge base.</p>"""
    knowledge_base_id: "capo_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier for the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeKnowledgeBaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeKnowledgeBaseRequest:
    out: DescribeKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    return out
