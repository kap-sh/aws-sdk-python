"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeKnowledgeBaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.knowledge_base
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeKnowledgeBaseResponse(TypedDict, closed=True):
    knowledge_base: "aws_sdk_quicksight.types.knowledge_base.KnowledgeBase"
    """<p>The knowledge base.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: NotRequired["aws_sdk_quicksight.types.status_code.StatusCode"]
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeKnowledgeBaseResponse) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.knowledge_base

    out["KnowledgeBase"] = aws_sdk_quicksight.types.knowledge_base.serialize_json(
        value["knowledge_base"]
    )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeKnowledgeBaseResponse:
    out: DescribeKnowledgeBaseResponse = {}  # type: ignore[typeddict-item]
    if "KnowledgeBase" in data:
        import aws_sdk_quicksight.types.knowledge_base

        out["knowledge_base"] = (
            aws_sdk_quicksight.types.knowledge_base.deserialize_json(
                data["KnowledgeBase"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeKnowledgeBaseResponse.knowledge_base required"
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
