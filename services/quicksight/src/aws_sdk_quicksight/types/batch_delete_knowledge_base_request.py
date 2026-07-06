"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDeleteKnowledgeBaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.batch_delete_knowledge_base_request_knowledge_base_ids_list
    import aws_sdk_quicksight.types.kb_aws_account_id


class BatchDeleteKnowledgeBaseRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.kb_aws_account_id.KbAwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the knowledge base.</p>"""
    knowledge_base_ids: "aws_sdk_quicksight.types.batch_delete_knowledge_base_request_knowledge_base_ids_list.BatchDeleteKnowledgeBaseRequestKnowledgeBaseIdsList"
    """<p>A list of knowledge base identifiers to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteKnowledgeBaseRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.batch_delete_knowledge_base_request_knowledge_base_ids_list

    out["KnowledgeBaseIds"] = (
        aws_sdk_quicksight.types.batch_delete_knowledge_base_request_knowledge_base_ids_list.serialize_json(
            value["knowledge_base_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteKnowledgeBaseRequest:
    out: BatchDeleteKnowledgeBaseRequest = {}  # type: ignore[typeddict-item]
    if "KnowledgeBaseIds" in data:
        import aws_sdk_quicksight.types.batch_delete_knowledge_base_request_knowledge_base_ids_list

        out["knowledge_base_ids"] = (
            aws_sdk_quicksight.types.batch_delete_knowledge_base_request_knowledge_base_ids_list.deserialize_json(
                data["KnowledgeBaseIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteKnowledgeBaseRequest.knowledge_base_ids required"
        )
    return out
