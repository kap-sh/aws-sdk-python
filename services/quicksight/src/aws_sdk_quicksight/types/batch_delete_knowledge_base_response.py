"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDeleteKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.batch_delete_knowledge_base_failure_list
    import aws_sdk_quicksight.types.batch_delete_knowledge_base_success_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class BatchDeleteKnowledgeBaseResponse(TypedDict):
    deleted: "aws_sdk_quicksight.types.batch_delete_knowledge_base_success_list.BatchDeleteKnowledgeBaseSuccessList"
    """<p>A list of knowledge bases that were successfully deleted.</p>"""
    errors: "aws_sdk_quicksight.types.batch_delete_knowledge_base_failure_list.BatchDeleteKnowledgeBaseFailureList"
    """<p>A list of knowledge bases that failed to be deleted.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: NotRequired["aws_sdk_quicksight.types.status_code.StatusCode"]
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteKnowledgeBaseResponse) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.batch_delete_knowledge_base_success_list

    out["Deleted"] = (
        aws_sdk_quicksight.types.batch_delete_knowledge_base_success_list.serialize_json(
            value["deleted"]
        )
    )
    import aws_sdk_quicksight.types.batch_delete_knowledge_base_failure_list

    out["Errors"] = (
        aws_sdk_quicksight.types.batch_delete_knowledge_base_failure_list.serialize_json(
            value["errors"]
        )
    )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> BatchDeleteKnowledgeBaseResponse:
    out: BatchDeleteKnowledgeBaseResponse = {}  # type: ignore[typeddict-item]
    if "Deleted" in data:
        import aws_sdk_quicksight.types.batch_delete_knowledge_base_success_list

        out["deleted"] = (
            aws_sdk_quicksight.types.batch_delete_knowledge_base_success_list.deserialize_json(
                data["Deleted"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteKnowledgeBaseResponse.deleted required")
    if "Errors" in data:
        import aws_sdk_quicksight.types.batch_delete_knowledge_base_failure_list

        out["errors"] = (
            aws_sdk_quicksight.types.batch_delete_knowledge_base_failure_list.deserialize_json(
                data["Errors"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteKnowledgeBaseResponse.errors required")
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
