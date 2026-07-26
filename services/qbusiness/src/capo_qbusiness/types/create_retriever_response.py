"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateRetrieverResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.retriever_arn
    import capo_qbusiness.types.retriever_id


class CreateRetrieverResponse(TypedDict, closed=True):
    retriever_id: NotRequired["capo_qbusiness.types.retriever_id.RetrieverId"]
    """<p>The identifier of the retriever you are using.</p>"""
    retriever_arn: NotRequired["capo_qbusiness.types.retriever_arn.RetrieverArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role associated with a retriever.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRetrieverResponse) -> dict:
    out: dict = {}
    if "retriever_id" in value:
        out["retrieverId"] = value["retriever_id"]
    if "retriever_arn" in value:
        out["retrieverArn"] = value["retriever_arn"]
    return out


def deserialize_json(data: dict) -> CreateRetrieverResponse:
    out: CreateRetrieverResponse = {}  # type: ignore[typeddict-item]
    if "retrieverId" in data:
        out["retriever_id"] = data["retrieverId"]
    if "retrieverArn" in data:
        out["retriever_arn"] = data["retrieverArn"]
    return out
