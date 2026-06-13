"""Generated from Smithy shape ``com.amazonaws.qconnect#GetKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.uuid_or_arn


class GetKnowledgeBaseRequest(TypedDict):
    knowledge_base_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKnowledgeBaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKnowledgeBaseRequest:
    out: GetKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    return out
