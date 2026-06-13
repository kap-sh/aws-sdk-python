"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeKnowledgeBasePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.kb_aws_account_id
    import aws_sdk_quicksight.types.knowledge_base_id


class DescribeKnowledgeBasePermissionsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.kb_aws_account_id.KbAwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the knowledge base.</p>"""
    knowledge_base_id: "aws_sdk_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier for the knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeKnowledgeBasePermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeKnowledgeBasePermissionsRequest:
    out: DescribeKnowledgeBasePermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
