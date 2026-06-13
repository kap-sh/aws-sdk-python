"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.knowledge_base_arn
    import aws_sdk_quicksight.types.knowledge_base_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DeleteKnowledgeBaseResponse(TypedDict):
    knowledge_base_arn: "aws_sdk_quicksight.types.knowledge_base_arn.KnowledgeBaseArn"
    """<p>The ARN of the deleted knowledge base.</p>"""
    knowledge_base_id: "aws_sdk_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The ID of the deleted knowledge base.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: NotRequired["aws_sdk_quicksight.types.status_code.StatusCode"]
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
