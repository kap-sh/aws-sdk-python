"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.knowledge_base_arn
    import capo_quicksight.types.knowledge_base_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DeleteKnowledgeBaseResponse(TypedDict, closed=True):
    knowledge_base_arn: "capo_quicksight.types.knowledge_base_arn.KnowledgeBaseArn"
    """<p>The ARN of the deleted knowledge base.</p>"""
    knowledge_base_id: "capo_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The ID of the deleted knowledge base.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: NotRequired["capo_quicksight.types.status_code.StatusCode"]
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKnowledgeBaseResponse) -> dict:
    out: dict = {}
    out["KnowledgeBaseArn"] = value["knowledge_base_arn"]
    out["KnowledgeBaseId"] = value["knowledge_base_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DeleteKnowledgeBaseResponse:
    out: DeleteKnowledgeBaseResponse = {}  # type: ignore[typeddict-item]
    if "KnowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["KnowledgeBaseArn"]
    else:
        raise DeserializationError(
            "DeleteKnowledgeBaseResponse.knowledge_base_arn required"
        )
    if "KnowledgeBaseId" in data:
        out["knowledge_base_id"] = data["KnowledgeBaseId"]
    else:
        raise DeserializationError(
            "DeleteKnowledgeBaseResponse.knowledge_base_id required"
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
